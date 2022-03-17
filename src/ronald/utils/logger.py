import logging

__all__ = [
    'logger',
    'get_logger',
    "set_level",
]


def set_level(_logger, log_level):
    _logger.setLevel(getattr(logging, log_level.upper()))


def get_logger(name, log_level='INFO'):
    _logger = logging.getLogger(name)
    _logger.propagate = False
    if len(_logger.handlers) > 0:
        return _logger
    log_handler = logging.StreamHandler()  # log to std.err
    fmt = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(filename)s:%(lineno)3s]: %(message)s')
    log_handler.setFormatter(fmt)
    _logger.addHandler(log_handler)
    set_level(_logger, log_level)
    return _logger


logger = get_logger('offline_tools')
