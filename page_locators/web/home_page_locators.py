#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 22:47
# @Author : 大山


class HomePageLocators:
    # 首页退出按钮定位
    logout_btn_locator = ('xpath', '//a[text()="退出"]')

    # 第一个标的【抢投标】
    first_bid_btn_loc = ('xpath', '//div[@class="b-unit-list clearfix"]/div[1]//a[text()="抢投标"]')