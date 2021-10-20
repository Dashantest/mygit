#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：home_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/6 17:17
from page_objects.base_page import BasePage
from page_locators.web.home_page_locators import HomePageLocators


class HomePage(BasePage):
    """
    把每个页面抽象成一个类，所有这个页面上的功能封装成方法
    """
    name = '登录成功首页'

    def get_logout_btn(self):
        """
        获取首页退出按钮
        :return:
        """
        ele = self.wait_element_is_visible(HomePageLocators.logout_btn_locator, '获取退出按钮').get_element()
        return ele

    def invest_first_bid(self):
        """
        选择第一个标
        :return:
        """
        self.wait_element_is_visible(HomePageLocators.first_bid_btn_loc, '选择第一个标').click_element()
