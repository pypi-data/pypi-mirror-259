from functools import wraps, partial
import os
import logging
import logging.config as log_conf
import time

log_dir = os.path.dirname(__file__) + '/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'retry.log')

log_config = {
    'version': 1.0,
    'formatters': {
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detail'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': log_path,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'crawler': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'parser': {
            'handlers': ['file'],
            'level': 'INFO',
        },
        'other': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
        },
        'storage': {
            'handlers': ['file'],
            'level': 'INFO',
        }
    }
}

log_conf.dictConfig(log_config)

r_logger = logging.getLogger('retry')


def retry(times=-1, delay=0, exceptions=Exception, logger=r_logger):
    """
    :param times: 重试次数
    :param delay: 重试间隔时间
    :param exceptions: 想要捕获的错误类型
    :param logger: 指定日志对象输出
    :return: func result or None
    """

    def _inter_retry(caller, retry_time, retry_delay, es):
        while retry_time:
            try:
                return caller()
            except es as e:
                retry_time -= 1
                if not retry_time:
                    logger.error("max tries for {} times, {} is raised, details: func name is {}, func args are {}".
                                 format(times, e, caller.func.__name__, (caller.args, caller.keywords)))
                    raise
                time.sleep(retry_delay)

    def retry_decorator(func):
        @wraps(func)
        def _wraps(*args, **kwargs):
            return _inter_retry(partial(func, *args, **kwargs), times, delay, exceptions)

        return _wraps

    return retry_decorator

# @retry()  # 默认无限重试
# def get_data():
#     print(1)
#     res = a + b  # 假设函数执行错误
#     return res
#
#
# res = get_data()
# print(res)

# @retry(5, 2)  # 重试5次，每隔2秒，如果都不成功，就抛出异常
# def get_data(self):
#     print(1)
#     res = 1 + 1  # 假设函数执行错误
#     return res
#
#
# res = get_data()
# print(res)
