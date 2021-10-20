#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：settings.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/6 8:57

import os

# 项目根目录
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE_DIR, 'testcases')
# 项目域名
POJECT_HOST = "http://8.129.91.152:8765"
# 接口信息
INTERFACE = {
    "login": "/Index/login.html"
}
# appium服务
APPIUM_SERVER_HOST = 'http://127.0.0.1:4723/wd/hub'
# app的desired_caps
DESIRED_CAPS = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "emulator-5554",
    "appPackage": "com.lemon.lemonban",
    "appActivity": ".activity.MainActivity",
    # "noReset": "true",  # 数据需要保存就设置为true
}
# 配置日志
# 路径拼接
# print(os.path.join(BASE_DIR, 'log', 'py34'))
LOG_CONGIF = {
    'name': __name__,
    'file': os.path.join(BASE_DIR, 'log', 'py34_web.log'),
    'fmt': '%(asctime)s-[%(filename)s-->line:%(lineno)d]-%(levelname)s:%(message)s',
    'debug': True
}
# web前程贷项目测试账户信息
TEST_NORMAL_USERNAME = "18684720553"
TEST_NORMAL_PASSWORD = "python"
# app柠檬班项目测试账户信息
TEST_USER = {
    'mobile': '18311424046',
    'password': '424046'
}

# 默认超时时间
DEFAULT_TIMEOUT = 5

# 错误截图路径
ERROR_SCREENSHOT_DIR = os.path.join(BASE_DIR, 'screenshot')