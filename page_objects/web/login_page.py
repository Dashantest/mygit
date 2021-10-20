#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：login_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/6 17:04
from page_objects.base_page import BasePage
from page_locators.web.login_page_locators import LoginPageLocators


class LoginPage(BasePage):
    """
    把每个页面抽象成一个类，所有这个页面上的功能封装成方法
    """
    name = '登录页面'

    def login(self, username, password):
        """
        登录页面的登录功能
        :param username:
        :param password:
        :return:
        """
        # 1.访问登录页面
        # BasePage中已经导入settings
        self.driver.get(self.settings.POJECT_HOST + self.settings.INTERFACE['login'])
        # 2.输入用户名、密码
        # 2.1定位用户名输入框
        # 2.2输入用户名
        self.wait_element_is_visible(LoginPageLocators.username_input_locator, '登录').send_keys(username)
        # 2.3定位密码输入框
        # 2.4输入密码
        self.wait_element_is_visible(LoginPageLocators.password_input_locator, '登录').send_keys(password)
        # 3.点击登录
        self.wait_element_is_visible(LoginPageLocators.login_btn_locator, '登录').click_element()
        # 如果实现self.wait_element_is_visible(LoginPageLocators.login_btn_locator, '登录').click_element()
        # 那么wait_element_is_visible(LoginPageLocators.login_btn_locator, '登录')必须返回self，此时用到链式编程
        # 将wait_element_is_visible()   return  self  且绑定属性element

    def get_error_tip(self):
        """
        获取错误信息
        :return:
        """
        # find_element需要by用*解包可以得到
        # return self.driver.find_element(*LoginPageLocators.error_info_tip_loc).text
        error_tip = self.wait_element_is_visible(LoginPageLocators.error_info_tip_loc, '获取错误信息').get_element_text()
        return error_tip


if __name__ == '__main__':
    from selenium import webdriver

    with webdriver.Chrome() as driver:
        lp = LoginPage(driver)
        lp.login('0000', '00000')
