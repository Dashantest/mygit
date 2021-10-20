#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：test_login_02.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/6 16:58
import pytest

from page_objects.web.login_page import LoginPage
from page_objects.web.home_page import HomePage
from testcases.base_test_case import BaseCase
from testdata.web.login_data import success_cases, fail_cases

"""
问题：1.断言部分不是很规范
      2.参数化
        2.1设计测试用例
      3.页面封装还有很多的漏洞
        3.1没有错误日志
        3.2还有很多冗余的代码
解决问题：1.自定义断言
"""


class TestLogin(BaseCase):
    name = '登录功能'


    # # 使用xunit风格的前置后置
    # @classmethod
    # def setup_class(cls):
    #     cls.logger.info('***********{}功能开始测试**********'.format(cls.name))
    #
    # @classmethod
    # def teardown_class(cls):
    #     cls.logger.info('***********{}功能测试结束**********'.format(cls.name))
    # 夹具就近原则，优先执行自己定义的夹具，在执行下面的driver夹具
    @pytest.mark.parametrize('case', fail_cases)
    def test_login_fail(self, driver, case):
        """
        测试登录功能
        :param driver:
        :return:
        """
        self.logger.info('+++++++++开始{}测试++++++++++'.format(case['title']))
        # 绑定driver对象，断言方法方便使用，断言要调用页面对象，而页面对象一定需要driver
        self.driver = driver
        # 实例化登录页面
        lp = LoginPage(driver)
        # 调用登录方法
        # BaseCase中已经导入了settings
        # lp.login('00000000000', self.settings.TEST_NORMAL_PASSWORD)
        # lp.login(case['request_data']['username'], case['request_data']['password'])
        lp.login(**case['request_data'])
        # 断言
        # 是在当前测试类中调用的check_login()，断言调用时还处于生命周期内
        # 断言需要：
        # 1.获取用例中check_data里的method方法然后执行
        # 2.判断执行结果是否和预期结果相等
        # 从某一个对象中动态的获取它的属性，用getattr()
        # method = getattr(self, case['check_data']['method'])
        # # 方法对象加()去执行，等价于执行这个方法
        # assert method() == case['check_data']['value']
        # 调用封装的断言
        self.my_assert(case['check_data'], case['title'])
        self.logger.info('+++++++++结束{}测试++++++++++'.format(case['title']))

    @pytest.mark.parametrize('case', success_cases)
    def test_login_success(self, driver, case):
        """
        测试登录功能
        :param driver:
        :return:
        """
        self.logger.info('+++++++++开始{}测试++++++++++'.format(case['title']))
        # 绑定driver对象，断言方法方便使用，断言要调用页面对象，而页面对象一定需要driver
        self.driver = driver
        # 实例化登录页面
        lp = LoginPage(driver)
        # 调用登录方法
        # BaseCase中已经导入了settings
        # lp.login('00000000000', self.settings.TEST_NORMAL_PASSWORD)
        # lp.login(case['request_data']['username'], case['request_data']['password'])
        lp.login(**case['request_data'])
        # 断言
        # 是在当前测试类中调用的check_login()，断言调用时还处于生命周期内
        # 断言需要：
        # 1.获取用例中check_data里的method方法然后执行
        # 2.判断执行结果是否和预期结果相等
        # 从某一个对象中动态的获取它的属性，用getattr()
        # method = getattr(self, case['check_data']['method'])
        # # 方法对象加()去执行，等价于执行这个方法
        # assert method() == case['check_data']['value']
        # 调用封装的断言
        self.my_assert(case['check_data'], case['title'])
        self.logger.info('+++++++++结束{}测试++++++++++'.format(case['title']))

    def check_login(self):
        """
        检查是否登录了
        :return:
        """
        hp = HomePage(self.driver)
        if hp.get_logout_btn():
            return True
        return False

    def get_error_tip(self):
        """
        获取错误信息
        :return:
        """
        lp = LoginPage(self.driver)
        return lp.get_error_tip()
