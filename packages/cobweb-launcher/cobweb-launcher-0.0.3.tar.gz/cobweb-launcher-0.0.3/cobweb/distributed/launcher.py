import time
import threading
from threading import Thread
from base.log import log
from db.base.redis_db import RedisDB
from base.bbb import Queue, Seed, DBItem
from base.utils import struct_queue_name, restore_table_name
from models import Scheduler, Spider, Storer


def start_seeds(seeds):
    if not seeds:
        return None
    if any(isinstance(seeds, t) for t in (list, tuple)):
        return [Seed(seed) for seed in seeds]
    elif any(isinstance(seeds, t) for t in (str, dict)):
        return Seed(seeds)


def parse_storer_info(storer_info):
    storer_data = {}
    storer_info_list = []
    if storer_info.__class__.__name__ == 'StorerInfo':
        storer_info_list.append(storer_info)
    elif any(isinstance(storer_info, t) for t in (list, tuple)):
        storer_info_list = storer_info
    for info in storer_info_list:
        db_name = info.DB.__name__
        storer_data.setdefault(db_name, {"StorerDB": info.DB, "db_args_list": []})
        storer_data[db_name]["db_args_list"].append(info[1:])
    return storer_data


def check(stop, last, spider, scheduler, storer_list, ready_seed_length, spider_queue_length):
    time.sleep(5)
    while True:
        if (
                scheduler.stop and
                not ready_seed_length() and
                not scheduler.queue.length and
                not spider.spider_in_progress.length
        ):
            log.info("spider is done?")
            last.set()
            time.sleep(5)
            storer_queue_empty = True
            for storer in storer_list:
                if storer.queue.length:
                    storer_queue_empty = False
                    break
            if storer_queue_empty and not spider_queue_length():
                log.info("spider done!")
                break
        last.clear()
        time.sleep(3)
    stop.set()


def launcher(task):
    """
    任务启动装饰器
    :param task: 任务配置信息
    """
    def decorator(func):
        """
        Item:
            Textfile()
            Loghub()
            Console()
        e.g.
        task.fields = "a,b"
        func(item, seed)
            a = "a"
            b = "b"
            data = {"a": "a", "b": "b"}
            yield item.Loghub(**data)
            yield item.Loghub(a=a, b=b)
        """
        storer_list = []

        # 程序结束事件
        last = threading.Event()
        # 停止采集事件
        stop = threading.Event()

        # 初始化redis信息
        redis_db = RedisDB(task.project, task.task_name, *task.redis_info)

        log.info("初始化cobweb!")

        seed_queue = Queue()

        # 调度器动态继承
        SchedulerDB, table, sql, length, size, config = task.scheduler_info
        SchedulerTmp = type(SchedulerDB.__name__, (Scheduler, SchedulerDB), {})

        # 初始化调度器
        scheduler = SchedulerTmp(table, sql, length, size, seed_queue, config)

        # 初始化采集器
        spider = Spider(seed_queue, task.max_retries)

        # 解析存储器信息
        storer_data = parse_storer_info(task.storer_info)

        # new item
        item = type("Item", (object,), {"redis_client": redis_db})()
        for db_name in storer_data.keys():
            # 存储器动态继承
            StorerDB = storer_data[db_name]["StorerDB"]
            StorerTmp = type(StorerDB.__name__, (Storer, StorerDB), {})
            db_args_list = storer_data[db_name]["db_args_list"]
            for storer_db_args in db_args_list:
                table, fields, length, config = storer_db_args
                if not getattr(item, db_name, None):
                    instance = type(db_name, (DBItem,), {})
                    setattr(item, db_name, instance)
                # 创建存储xxx, 创建存储队列
                storer_item_instance = getattr(item, db_name)
                storer_item_instance.init_item(table, fields)
                #
                storer_queue = struct_queue_name(db_name, table)
                queue = getattr(storer_item_instance, storer_queue)
                # 初始话存储器
                table_name = restore_table_name(table_name=table)
                storer = StorerTmp(table_name, fields, length, queue, config)
                storer_list.append(storer)

        Thread(target=redis_db.check_spider_queue, args=(stop, len(storer_list))).start()
        Thread(target=redis_db.set_heartbeat, args=(stop,)).start()

        # 推送初始种子
        seeds = start_seeds(task.start_seed)
        redis_db.add_seed(seeds)
        # 启动调度器, 调度至redis队列
        Thread(
            # name="xxxx_schedule_seeds",
            target=scheduler.schedule_seed,
            args=(
                redis_db.ready_seed_length,
                redis_db.get_scheduler_lock,
                redis_db.add_seed
            )
        ).start()

        # 启动调度器, 调度任务队列
        Thread(
            # name="xxxx_schedule_task",
            target=scheduler.schedule_task,
            args=(
                stop, redis_db.get_seed,
                redis_db.ready_seed_length
            )
        ).start()

        # 启动采集器
        for index in range(task.spider_num):
            Thread(
                # name=f"xxxx_spider_task:{index}",
                target=spider.spider_task,
                args=(
                    stop, func, item,
                    redis_db.del_seed
                )
            ).start()

        # 启动存储器
        for storer in storer_list:
            Thread(
                # name=f"xxxx_store_task:{storer.table}",
                target=storer.store_task,
                args=(
                    stop, last,
                    redis_db.reset_seed,
                    redis_db.set_storer
                )
            ).start()

        Thread(
            # name="check_spider",
            target=check,
            args=(
                stop, last, spider,
                scheduler, storer_list,
                redis_db.ready_seed_length,
                redis_db.spider_queue_length,
            )
        ).start()

    return decorator




