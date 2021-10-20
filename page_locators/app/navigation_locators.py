#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：navigation_locators.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:52
from appium.webdriver.common.mobileby import MobileBy as By


class NavigationLocators:
    # 主页
    home_loc = (By.ID, 'com.lemon.lemonban:id/navigation_home')
    # 题库
    tiku_loc = (By.ID, 'com.lemon.lemonban:id/navigation_tiku')
    # 我的
    my_loc = (By.ID, 'com.lemon.lemonban:id/navigation_my')