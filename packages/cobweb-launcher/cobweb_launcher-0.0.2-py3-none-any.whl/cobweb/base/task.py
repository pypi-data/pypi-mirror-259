from config import info


class Task:

    def __init__(
            self,
            project=None,
            task_name=None,
            start_seed=None,
            spider_num=None,
            # queue_length=None,
            max_retries=None,
            scheduler_info=None,
            storer_info=None,
            redis_info=None
    ):
        """

        :param project:
        :param task_name:
        :param start_seed:
        :param spider_num:
        # :param queue_length:
        :param scheduler_info:
        :param storer_info: Union(list, DataInfo/namedtuple), 单个元素构成必须有3个值(数据库类型，表名，字段名)
        """
        self.project = project or "test"
        self.task_name = task_name or "spider"
        self.start_seed = start_seed
        self.spider_num = spider_num or 1
        self.max_retries = max_retries or 5
        # self.redis_info = RedisInfo(**(redis_info or dict()))
        self.redis_info = info(redis_info, tag=0)
        # self.scheduler_info = SchedulerDB.info(scheduler_info)
        self.scheduler_info = info(scheduler_info, tag=1)
        # self.storer_info = StorerDB.info(storer_info)
        self.storer_info = info(storer_info, tag=2)
