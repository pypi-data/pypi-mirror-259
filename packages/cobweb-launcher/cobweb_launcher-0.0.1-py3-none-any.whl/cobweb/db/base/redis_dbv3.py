import json
import random
import time
import redis
from datetime import datetime
from base.bbb import Seed


class RedisDB:

    def __init__(
            self,
            project: str,
            task_name: str,
            # retry_num: int = 3,
            host=None,
            port=None,
            username=None,
            password=None,
            db=0
    ):
        pool = redis.ConnectionPool(
            host=host,
            port=port,
            username=username,
            password=password,
            db=db
        )
        self.heartbeat_key = f"{project}:{task_name}:heartbeat"  # redis type string
        self.ready_key = f"{project}:{task_name}:seed_info:ready"  # redis type zset, .format(priority)
        self.spider_key = f"{project}:{task_name}:seed_info:spider"  # redis type hash, .format(priority)
        self.store_key = f"{project}:{task_name}:seed_info:store:%s"  # redis type set,
        self.failed_key = f"{project}:{task_name}:seed_info:failed"  # redis type set, .format(priority)
        self.succeed_key = f"{project}:{task_name}:seed_info:succeed"  # redis type set, .format(priority)
        self.update_lock = f"{project}:{task_name}:update_seed_lock"  # redis type string
        self.check_lock = f"{project}:{task_name}:check_seed_lock"  # redis type string
        # self.retry_lock = f"{project}:{task_name}:retry_seed_lock"  # redis type string
        self.scheduler_lock = f"{project}:{task_name}:scheduler_lock"  # redis type string
        self.client = redis.Redis(connection_pool=pool)
        # self.retry_num = retry_num

    def set_heartbeat(self, t=3):
        self.client.expire(self.heartbeat_key, t)

    # @property
    def heartbeat(self):
        return self.client.ttl(self.heartbeat_key)

    def iterate_hash(self, key, count=1000, match=None):
        cursor = "0"
        while cursor != 0:
            # 使用HSCAN命令迭代获取键值对
            cursor, data = self.client.hscan(key, cursor=cursor, match=match, count=count)
            if not data:
                return None
            for field, value in data.items():
                yield field.decode(), value.decode()

    def get_lock(self, key, t=15, timeout=3, sleep_time=0.1):
        begin_time = int(time.time())
        while True:
            if self.client.setnx(key, ""):
                self.client.expire(key, t)
                return True
            if int(time.time()) - begin_time > timeout:
                break
            time.sleep(sleep_time)

        if self.client.ttl(key) == -1:
            delete_status = True
            for _ in range(3):
                if self.client.ttl(key) != -1:
                    delete_status = False
                    break
                time.sleep(0.5)
            if delete_status:
                self.client.expire(key, t)
            return False
        else:
            ttl = self.client.ttl(key)
            print("ttl: " + str(ttl))
            return False

    def execute_update(
            self,
            set_info,
            del_info,
            status: int = 0
    ):
        if status not in [0, 1, 2, 3]:
            return None

        pipe = self.client.pipeline()
        pipe.multi()

        if status == 0:
            pipe.hset(self.spider_key, mapping=set_info)
            pipe.zrem(self.ready_key, *del_info)
        elif status == 1:
            pipe.zadd(self.ready_key, mapping=set_info)
            pipe.hdel(self.spider_key, *del_info)
        elif status == 2:
            pipe.sadd(self.failed_key, *set_info)
            pipe.hdel(self.spider_key, *del_info)
        else:
            pipe.sadd(self.succeed_key, *set_info)
            pipe.hdel(self.spider_key, *del_info)
        pipe.execute()

    @property
    def seed_count(self):
        return self.client.zcard(self.ready_key)

    def deal_seeds(self, sids, status: bool):
        if isinstance(sids, str):
            sids = [sids]
        # if self.get_lock(key=self.retry_lock, t=15):
        status = 2 if status else 3
        del_list, fail_set = [], set()
        for sid in sids:
            for field, value in self.iterate_hash(self.spider_key, match=f"*{sid}"):
                _, priority, _sid = field.split("_")
                if sid != _sid:
                    continue
                seed = Seed(value, priority=priority)
                del_list.append(field)
                fail_set.add(seed.format_seed)
            if del_list:
                self.execute_update(fail_set, del_list, status=status)
            # self.client.delete(self.retry_lock)
            print("retry seeds, sids: {}".format(json.dumps(sids)))

    def set_seeds(self, seeds):
        item_info = {}
        if any(isinstance(seeds, t) for t in (list, tuple)):
            for seed in seeds:
                item_info[seed.format_seed] = seed.priority
        elif isinstance(seeds, Seed):
            item_info[seeds.format_seed] = seeds.priority
        self.client.zadd(self.ready_key, mapping=item_info)

    def get_seeds(self, length: int = 1000):
        """
        redis获取种子
        """
        cs = time.time()

        if self.get_lock(key=self.update_lock):

            set_dict, del_list, result = {}, [], []

            # version = int(time.time() * 1e3)
            version = time.time() * 1e6

            items = self.client.zrangebyscore(self.ready_key, min=0, max="+inf", start=0, num=length, withscores=True)

            # for value, priority in items:
            #     seed = Seed(value, priority=priority, version=version)
            #     pty = "{:03d}".format(int(priority))
            #     key = f"{version}_{pty}_{seed.sid}"
            #     set_dict[key] = value
            #     del_list.append(value)
            #     result.append(seed)

            for value, priority in items:
                v = version + int(priority) / 1000 + random.random() / 1000
                seed = Seed(value, priority=priority, version=version)
                pty = "{:03d}".format(int(priority))
                key = f"{version}_{pty}_{seed.sid}"
                set_dict[key] = value
                del_list.append(value)
                result.append(seed)

            print("\nset seeds into queue time: " + str(time.time() - cs))
            if result:
                self.execute_update(set_dict, del_list)

            self.client.delete(self.update_lock)
            print("push seeds into queue time: " + str(time.time() - cs))
            return result

    def check_spider_hash(self):
        cs = time.time()
        set_dict, del_list, heartbeat = {}, [], False
        if self.get_lock(key=self.check_lock, t=60, timeout=600, sleep_time=60):
            count = self.client.hlen(self.spider_key)
            if self.client.exists(self.heartbeat_key):
                heartbeat = True
            now = int(time.time())
            for field, value in self.iterate_hash(key=self.spider_key, count=count):
                version, priority, sid = field.split("_")
                if heartbeat and int(version) + 600 > now:
                    continue
                set_dict[value] = priority
                del_list.append(field)

                if len(del_list) >= 1000:
                    self.client.expire(self.check_lock, 60)
                    self.execute_update(set_dict, del_list, status=1)
                    set_dict, del_list = {}, []

            if set_dict and del_list:
                self.execute_update(set_dict, del_list, status=1)

            # self.client.delete(self.check_lock)
            print("init seeds time: " + str(time.time() - cs))
            if not heartbeat:
                self.client.setnx(self.heartbeat_key, "")
                self.set_heartbeat(t=15)

    def add_store_sid(self, key, data):
        redis_key = self.store_key % key
        self.client.sadd(redis_key, *data)


current_time = datetime.now()
# 格式化日期时间字符串
formatted_time = current_time.strftime("%m%d%H%M%S%f")
c = int(formatted_time)
print(c)
d = 200 + 0.9 * random.random()
print(d)
print(time.time())
print(c + d / 1000)
# for _ in range(100):
#     redis_db.get_seeds(1000)
# redis_db.get_seeds(1000)
# redis_db.check_spider_hash()
# redis_db.retry_seeds(["dc895aee47f8fc39c479f7cac6025879"])
# "1705996980_200_dc895aee47f8fc39c479f7cac6025879"

