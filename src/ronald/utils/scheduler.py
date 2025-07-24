'''
Author: RonaldSun a297131009@qq.com
Date: 2022-06-20 15:50:12
LastEditors: RonaldSun a297131009@qq.com
LastEditTime: 2022-10-11 21:46:42
'''
from ronald.utils.common_include import *
from ronald.utils.logger import *
import functools
import time


def retry_if_fail(max_retry_times=5, sleep_time=0, print_trace=True):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            for _ in range(max_retry_times):
                try:
                    return func(*args, **kw)
                except Exception as e:
                    if print_trace:
                        logger.warning(f"An error occurred: {e}")
                    logger.warning("waiting for retry...")
                    sleep(sleep_time)
            return None
        return wrapper
    return decorator


def sleep(wait_sec=5):
    wait_time = wait_sec
    logger.info("wait_time: {}".format(wait_time))
    time.sleep(wait_time)
