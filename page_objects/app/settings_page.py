#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：settings_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 17:09
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.setttings_page_locators import SettingsPageLocators



class SettingsPage(AppBasePage):
    name = '设置页面'

    def logout(self):
        """
        点击退出按钮，退出登录
        :return:
        """
        self.wait_element_is_visible(SettingsPageLocators.logout_btn_loc, '点击退出').click_element()

    def click_confirm(self):
        """
        点击确认
        :return:
        """
        self.wait_element_is_visible(SettingsPageLocators.sure_btn_loc, '点击确认').click_element()

    def get_logout_toast(self):
        """
        获取退出后的toast
        :return:
        """
        return self.wait_element_is_loaded(SettingsPageLocators.logout_toast_loc, '登出后toast').get_element_text()