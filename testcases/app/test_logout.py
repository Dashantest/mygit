#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：test_logout.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 16:22
from testcases.base_test_case import BaseCase
from page_objects.app.navigation_page import NavigationPage
from page_objects.app.my_page import MyPage
from page_objects.app.settings_page import SettingsPage



class TestLogout(BaseCase):
    name = '登出功能'

    def test_logout(self, signed_in_driver):
        self.logger.info('**********{}开始测试**********'.format(self.name))
        # 前置为已登录，通过夹具实现
        # 点击我的柠檬，保证后面可以定位到设置
        self.driver = signed_in_driver
        np = NavigationPage(signed_in_driver)
        np.click_my()
        # 点击设置
        mp = MyPage(signed_in_driver)
        mp.enter_settings_page()
        # 点击退出
        sp = SettingsPage(signed_in_driver)
        sp.logout()
        # 点击弹框的确认
        sp.click_confirm()
        # 断言
        self.assert_equal(sp.get_logout_toast(), '退出登录成功')
        self.logger.info('**********{}测试结束**********'.format(self.name))