# -*- coding: utf-8 -*-

import logging
import time
import sys

def get_logger(name, console_log = True, file_log = True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)  # 设置默认日志等级
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
    if console_log:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter
        logger.addHandler(console_handler)
    if file_log:
        # file_handler = logging.FileHandler(name + time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime()) + ".log")
        file_handler = logging.FileHandler(name + ".log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger