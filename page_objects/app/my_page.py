#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：my_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 15:41
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.my_page_locators import MyPageLocators



class MyPage(AppBasePage):
    name = '我的柠檬页面'

    def enter_login_page(self):
        """
        点击我的头像，进入登录页面
        :return:
        """
        self.wait_element_is_visible(MyPageLocators.login_page_loc, '点击我的头像，进入登录页面').click_element()

    def my_lemon_avatar_title(self):
        """
        获取登录成功后的昵称
        :return:
        """
        return self.wait_element_is_visible(MyPageLocators.my_lemon_title_loc, '获取登录成功后昵称').get_element_text()

    def enter_settings_page(self):
        """
        点击我的页面（已登录）的设置
        :return:
        """
        self.wait_element_is_visible(MyPageLocators.settings_btn_loc, '点击设置按钮').click_element()

    def get_login_out_toast(self):
        """
        获取登出成功后的toast
        :return:
        """
        return self.wait_element_is_loaded(MyPageLocators.login_out_toast_loc, '获取登出提示信息').get_element_text()