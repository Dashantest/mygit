#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 22:47
# @Author : 大山

class LoginPageLocators:
    # 用户名输入框定位
    username_input_locator = ('xpath', '//input[@name="phone"]')
    # 密码输入框定位
    password_input_locator = ('xpath', '//input[@name="password"]')
    # 登录按钮定位
    login_btn_locator = ('xpath', '//button[text()="登录"]')
    # 错误信息定位
    error_info_tip_loc = ('xpath', '//div[@class="form-error-info"]')
