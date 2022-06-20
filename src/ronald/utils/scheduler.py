'''
Author: LinSu(lin.su@nio.com)
Date: 2022-06-20 15:50:12
LastEditors: LinSu(lin.su@nio.com)
LastEditTime: 2022-06-20 19:51:16
'''
from ronald.utils.common_include import *
from ronald.utils.logger import *
import functools
import time


def retry_if_fail(max_retry_times=5, sleep_time=0):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for _ in range(max_retry_times):
                try:
                    return func(*args, **kw)
                except:
                    logger.warning("waiting for retry...")
                    sleep(sleep_time)
            return None
        return wrapper
    return decorator


def sleep(wait_sec=5):
    wait_time = wait_sec
    logger.info("wait_time: {}".format(wait_time))
    time.sleep(wait_time)
