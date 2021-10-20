#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_page_locators.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 16:13
from appium.webdriver.common.mobileby import MobileBy as By



class LoginPageLocators:
    # 用户名输入框
    username_input_loc = (By.ID, 'com.lemon.lemonban:id/et_mobile')
    # 密码输入框
    password_input_loc = (By.ID, 'com.lemon.lemonban:id/et_password')
    # 登录按钮
    submit_btn_loc = ('xpath', '//*[@text="登录"]')
    # 关闭登录图标
    close_btn_loc = ('xpath', '//*[@class="android.widget.ImageButton"]')
