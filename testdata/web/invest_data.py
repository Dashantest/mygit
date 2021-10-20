#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 23:46
# @Author : 大山
# 成功用例
success_cases = [
    {
        'title': "投资100成功",
        'request_data': {"amount": 100},
        'check_data': {"method": "invest_success", "value": True}
    },
    {
        'title': "投资200成功",
        'request_data': {"amount": 200},
        'check_data': {"method": "invest_success", "value": True}
    },
    {
        'title': "投资500成功",
        'request_data': {"amount": 500},
        'check_data': {"method": "invest_success", "value": True}
    },
]

fail_cases = [

    {
        'title': "投资金额为0",
        'request_data': {"amount": 0},
        'check_data': {"method": "get_pop_error_tip", "value": "请正确填写投标金额"}
    },
    {
        'title': "投资金额为负数",
        'request_data': {"amount": -100},
        'check_data': {"method": "get_pop_error_tip", "value": "请正确填写投标金额"}
    },
    {
        'title': "投资金额大于标的可投金额",
        'request_data': {"amount": 10000000},
        'check_data': {"method": "get_pop_error_tip", "value": "购买标的金额不能大于标剩余金额"}
    },
]
