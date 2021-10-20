#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 22:47
# @Author : 大山


class BidPageLocators:
    """
    标的页面定位信息
    """
    # 投资输入框
    invest_input_loc = ('xpath', '//input[@class="form-control invest-unit-investinput"]')
    # 投资按钮
    invest_btn = ('xpath', '//button[text()="投标"]')
    # 弹框错误信息提示
    error_tip_loc = ('xpath', '//div[@class="text-center"]')
    # 获取投资成功弹框的标识
    success_pop_btn_loc = ('xpath', '//div[contains(@id,"layui-layer")]//button[text()="查看并激活"]')