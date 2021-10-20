#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：test_login.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:48
import pytest

from testcases.base_test_case import BaseCase
from testdata.app.login_data import fail_cases, success_cases
from page_objects.app.login_page import LoginPage
from page_objects.app.my_page import MyPage


class TestLogin(BaseCase):
    name = '登录lemon'

    @pytest.mark.parametrize('case', fail_cases)
    def test_login_fail(self, to_my_page_driver, case):
        self.logger.info('**********{}开始测试**********'.format(case['title']))
        self.driver = to_my_page_driver
        # 点击我的头像，进入登录页面
        mp = MyPage(to_my_page_driver)
        mp.enter_login_page()
        # 登录页面，调登录方法
        lp = LoginPage(to_my_page_driver)
        lp.login(**case['request_data'])
        # 断言实际错误信息与预期错误信息
        try:
            self.assert_equal(case['error_msg'], lp.get_toast_msg())
        except Exception as e:
            self.logger.exception('{}断言【失败】，预期结果为：{},实际结果为：{}'.format(
                case['title'], case['error_msg'], lp.get_toast_msg()))
            raise e
        finally:
            # 每次执行完无论成功或者失败都关闭登录页面，因为Android的特性，如果页面不刷新，toast还是原来的
            lp.close_login_page()
        self.logger.info('**********{}测试结束**********'.format(case['title']))

    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, to_my_page_driver, case):
        self.logger.info('**********{}开始测试**********'.format(case['title']))
        self.driver = to_my_page_driver
        # 点击我的头像，进入登录页面
        mp = MyPage(to_my_page_driver)
        mp.enter_login_page()
        # 登录页面，调登录方法
        lp = LoginPage(to_my_page_driver)
        lp.login(**case['request_data'])
        # 断言，获取昵称是否与实际昵称一致
        self.assert_equal(case['avatar_title'], mp.my_lemon_avatar_title())
        # 每次执行完关闭登录页面
        lp.close_login_page()
        self.logger.info('**********{}测试结束**********'.format(case['title']))
