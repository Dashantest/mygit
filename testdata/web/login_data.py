#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_data.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/8 10:57

# 正向用例
success_cases = [
    {
        "title": "登录成功",
        "request_data": {"username": "18684720553", "password": "python"},
        "check_data": {"method": "check_login", "value": True}
    }
]
# 反向用例
fail_cases = [
    {
        "title": "手机号为空",
        "request_data": {"username": "", "password": "python"},
        "check_data": {"method": "get_error_tip", "value": "请输入手机号"}
    },
    {
        "title": "手机输入有误",
        "request_data": {"username": "123", "password": "python"},
        "check_data": {"method": "get_error_tip", "value": "请输入正确的手机号"}
    },
    {
        "title": "密码为空",
        "request_data": {"username": "18684720553", "password": ""},
        "check_data": {"method": "get_error_tip", "value": "请输入密码"}
    }
]
