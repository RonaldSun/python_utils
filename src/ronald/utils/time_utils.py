from ronald.utils.common_include import *
from datetime import datetime, timedelta


def CalcTimeDiff(datetime: timedelta):
    time_diff = datetime.days * 86400 + datetime.seconds + datetime.microseconds / 1e6
    return time_diff
