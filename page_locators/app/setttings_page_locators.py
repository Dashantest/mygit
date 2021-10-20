#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：setttings_page_locators.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/26 17:14
from appium.webdriver.common.mobileby import MobileBy


class SettingsPageLocators:
    # 退出按钮
    logout_btn_loc = (MobileBy.ID, 'com.lemon.lemonban:id/logout_button')
    # 确认按钮
    sure_btn_loc = (MobileBy.ID, 'com.lemon.lemonban:id/tv_sure')
    # 登出成功的toast
    logout_toast_loc = ('xpath', '//*[@class="android.widget.Toast"]')