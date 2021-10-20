#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 16:11
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.login_page_locators import LoginPageLocators


class LoginPage(AppBasePage):
    """
    把每个页面抽象成一个类，所有这个页面上的功能封装成方法
    """
    name = '登录页面'

    def login(self, mobile, password):
        """
        登录页面的登录功能
        :param mobile:
        :param password:
        :return:
        """
        # 2.2输入用户名
        self.wait_element_is_visible(LoginPageLocators.username_input_loc, '登录').send_keys(mobile)
        # 2.3定位密码输入框
        # 2.4输入密码
        self.wait_element_is_visible(LoginPageLocators.password_input_loc, '登录').send_keys(password)
        # 3.点击登录
        self.wait_element_is_visible(LoginPageLocators.submit_btn_loc, '登录').click_element()

    def close_login_page(self):
        """
        关闭登录页面
        :return:
        """
        self.wait_element_is_visible(LoginPageLocators.close_btn_loc, '关闭登录页面').click_element()
