#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：my_page_locators.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 16:38
from appium.webdriver.common.mobileby import MobileBy



class MyPageLocators:
    # 点击头像，进入登录页面
    login_page_loc = ('xpath', '//*[@text="点击头像登录"]')
    # 获取登录成功后的昵称
    my_lemon_title_loc = (MobileBy.ID, 'com.lemon.lemonban:id/fragment_my_lemon_avatar_title')
    # 获取登出成功后的toast
    login_out_toast_loc = ('xpath', '//*[@class="android.widget.Toast"]')
    # 设置按钮
    settings_btn_loc = ('xpath', '//*[@class="android.widget.ImageButton"]')