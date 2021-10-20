#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/11/18 1:17
# @Author : 大山
"""
日志组件
1.  loggers  日志器，产生日志
2.  Handler  日志处理器，将日志发送到指定位置，文件中/控制台
3.  Filter   日志过滤器
4.Formatter  日志格式器，用于控制日志的输出格式
"""

# 日志步骤
# 1.创建日志器，设置等级
# import logging
# logger = logging.getLogger('python34') # 日志器的名字
# logger.setLevel(logging.DEBUG)
# # 2.创建日志处理器
# # 文件
# file_handler = logging.FileHandler(filename='py34.log', encoding='utf-8')
# file_handler.setLevel(logging.WARNING)  # 设置写入文件等级
# # 控制台
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# # 3.创建格式化器
# formatter = logging.Formatter(fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s')
# # 4.把格式化器添加到处理器上
# # 可以给文件和控制台自定义，这里使用同一格式化器
# file_handler.setFormatter(formatter)
# console_handler.setFormatter(formatter)
# # 5.把日志处理器添加到日志器
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)
import logging
from settings import LOG_CONGIF


def get_logger(name=__name__, file='py34_web.log', fmt='%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s', debug=False):
    """
    封装一个获取日志的方法
    :param name: 日志名称，默认谁调用，名称就是谁
    :param file: 日志写入文件名称，默认‘py34_web.log’
    :param debug: 默认False
    :return:返回一个logger
    """
    if debug:
        # 如果开启调试模式（debug），就打印所有日志到指定文件和控制台
        # file_level文件等级  console_level控制台等级
        file_level = logging.DEBUG
        console_level = logging.DEBUG
    else:
        file_level = logging.WARNING
        console_level = logging.INFO
    # 1.创建日志器，设置等级
    logger = logging.getLogger(name) # 日志器的名字
    logger.setLevel(logging.DEBUG)
    # 2.创建日志处理器
    # 文件
    file_handler = logging.FileHandler(filename=file, encoding='utf-8')
    file_handler.setLevel(file_level)  # 设置写入文件等级
    # 控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(console_level)
    # 3.创建格式化器
    formatter = logging.Formatter(fmt=fmt)
    # 4.把格式化器添加到处理器上
    # 可以给文件和控制台自定义，这里使用同一格式化器
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # 5.把日志处理器添加到日志器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger


# 用变量logger接受get_logger()方便调用，如果修改，在下方修改即可
logger = get_logger(**LOG_CONGIF)

if __name__ == '__main__':
    logger.info('---+++++++++++')