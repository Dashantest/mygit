#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_data.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:59

# 正向用例
success_cases = [
    {
        "title": "登录成功",
        "request_data": {"mobile": "18311424046", "password": "424046"},
        "avatar_title": "北京-大山"
    }
]
# 反向用例
fail_cases = [
    {
        "title": "用户名为空",
        "request_data": {"mobile": "", "password": "424046"},
        "error_msg": "手机号码或密码不能为空"
    },
    {
        "title": "手机号输入有误",
        "request_data": {"mobile": "18311424047", "password": "424046"},
        "error_msg": "错误的账号信息"
    },
    {
        "title": "密码为空",
        "request_data": {"mobile": "18311424046", "password": ""},
        "error_msg": "手机号码或密码不能为空"
    },
]
