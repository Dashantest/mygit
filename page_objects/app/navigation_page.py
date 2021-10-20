#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：navigation_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 15:32
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.navigation_locators import NavigationLocators as NavLoc


class NavigationPage(AppBasePage):
    name = '导航栏'

    def switch_navigation(self, nav_name):
        """
        获取名称为nav_name的页面
        :param nav_name:
        :return:
        """
        if nav_name == '主页':
            self.wait_element_is_visible(NavLoc.home_loc, '主页').click_element()
        elif nav_name == '题库':
            self.wait_element_is_visible(NavLoc.tiku_loc, '题库').click_element()
        elif nav_name == '我的柠檬':
            self.wait_element_is_visible(NavLoc.my_loc, '我的柠檬').click_element()
        else:
            raise ValueError('导航栏没有这个菜单')

    def click_my(self):
        """
        点击我的，即切换至我的
        :return:
        """
        self.wait_element_is_visible(NavLoc.my_loc, '点击我的').click_element()
