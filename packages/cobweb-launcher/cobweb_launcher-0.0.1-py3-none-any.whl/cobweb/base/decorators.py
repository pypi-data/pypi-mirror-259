import time
from functools import wraps

# from config import DBType
from log import log


# def find_func_name(func_name, name_list):
#     for name in name_list:
#         if func_name.find(name) == 0:
#             return True
#     return False


# def starter_decorator(execute):
#     @wraps(execute)
#     def wrapper(starter, *args, **kwargs):
#         spider_dynamic_funcs = []
#         scheduler_dynamic_funcs = []
#         starter_functions = inspect.getmembers(starter, lambda a: inspect.isfunction(a))
#         for starter_function in starter_functions:
#             if find_func_name(starter_function[0], starter.scheduler_funcs):
#                 scheduler_dynamic_funcs.append(starter_function)
#             elif find_func_name(starter_function[0], starter.spider_funcs):
#                 spider_dynamic_funcs.append(starter_function)
#         return execute(starter, scheduler_dynamic_funcs, spider_dynamic_funcs, *args, **kwargs)
#
#     return wrapper


# def scheduler_decorator(execute):
#     @wraps(execute)
#     def wrapper(scheduler, distribute_task):
#         if not issubclass(scheduler, SchedulerInterface):
#             scheduler.stop = True
#         elif getattr(scheduler, "scheduler", None):
#             execute(scheduler, distribute_task)
#         else:
#             log.error(f"scheduler type: {scheduler.db_type} not have add function!")
#             scheduler.stop = True
#     return wrapper


def storer_decorator(execute):
    @wraps(execute)
    def wrapper(storer, stop_event, last_event, table_name, callback):
        if getattr(storer, "save", None):
            execute(storer, stop_event, last_event, table_name, callback)
        else:
            log.error(f"storer base_type: {storer.data_type} not have add function!")
            storer.stop = True
    return wrapper


def distribute_scheduler_decorators(func):
    @wraps(func)
    def wrapper(distributor, callback):
        try:
            func(distributor, callback)
        except TypeError:
            pass
        distributor.event.set()
    return wrapper


def distribute_spider_decorators(func):
    @wraps(func)
    def wrapper(distributor, stop_event, db, callback):
        while not stop_event.is_set():
            try:
                seed = distributor.queue_client.pop("_seed_queue")
                if not seed:
                    time.sleep(3)
                    continue
                distributor.spider_in_progress.append(1)
                func(distributor, db, seed, callback)
            except Exception as e:
                print(e)
            finally:
                distributor.spider_in_progress.pop()

    return wrapper


def distribute_storer_decorators(func):
    @wraps(func)
    def wrapper(distributor, callback, data_type, table_name, last):
        data_list = []
        try:
            func(distributor, callback, data_list, data_type, table_name, last)
        except Exception as e:
            log.info("storage exception! " + str(e))
            # distributor._task_queue.extendleft(data_list)

    return wrapper
