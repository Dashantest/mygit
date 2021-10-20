#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 22:35
# @Author : 大山
import pytest

from testcases.base_test_case import BaseCase
from page_objects.web.home_page import HomePage
from page_objects.web.bid_page import BidPage
from testdata.web.invest_data import success_cases, fail_cases


class TestInvest(BaseCase):
    name = '投资功能'

    @pytest.mark.parametrize('case', fail_cases)
    def test_invest_fail(self, login_driver, case):
        self.logger.info('********{}开始测试*********'.format(case['title']))
        # 因为操作一致，所以可以进行参数化（如果操作不一致需要单独写）
        # 每次进来都需要访问一下首页，不然会在标的页面，定位不到第一个标
        login_driver.get(self.settings.POJECT_HOST)
        # 绑定driver  供check使用
        self.driver = login_driver
        # 1.登录（写到夹具里）,要使用夹具的返回值，就传参
        # 2.选择一个标，点击进入详情（首页页面的页面逻辑）
        hp = HomePage(login_driver)
        hp.invest_first_bid()
        # 3.投标 （标页面，页面逻辑，再封装）
        bp = BidPage(login_driver)
        # bp.invest(case['request_data']['amount'])
        bp.invest(**case['request_data'])
        # 4.断言
        # assert bp.get_pop_error_tip() == case['check_data']['value']
        self.my_assert(case['check_data'], case['title'])
        self.logger.info('********{}测试结束*********'.format(case['title']))

    @pytest.mark.success  # 打标记
    @pytest.mark.parametrize('case', success_cases)
    def test_invest_success(self, login_driver, case):
        self.logger.info('********{}开始测试*********'.format(case['title']))
        # 因为操作一致，所以可以进行参数化（如果操作不一致需要单独写）
        # 每次进来都需要访问一下首页，不然会在标的页面，定位不到第一个标
        login_driver.get(self.settings.POJECT_HOST)
        # 绑定driver  供check使用
        self.driver = login_driver
        # 1.登录（写到夹具里）,要使用夹具的返回值，就传参
        # 2.选择一个标，点击进入详情（首页页面的页面逻辑）
        hp = HomePage(login_driver)
        hp.invest_first_bid()
        bp = BidPage(login_driver)
        # 3.获取用户投资前余额
        user_balance_before_invest = bp.get_user_balance()
        # 4.获取标的的投资前可投资额
        bid_balance_before_invest = bp.get_bid_balance()
        # 5.投标 （标页面，页面逻辑，再封装）
        bp.invest(**case['request_data'])
        # 6.断言
        # assert bp.get_pop_error_tip() == case['check_data']['value']
        self.my_assert(case['check_data'], case['title'])
        # 刷新页面，否则前程贷项目中，无法获取标的的投资后可投资额
        login_driver.refresh()
        # sql校验，导入之前的db模块，进行校验
        # 校验余额
        # 7.获取用户投资后余额
        user_balance_after_invest = bp.get_user_balance()
        # 8.获取标的的投资后可投资额
        bid_balance_after_invest = bp.get_bid_balance()
        # 用户投资前余额 - 用户投资后余额 = 投资额
        self.assert_equal(
            user_balance_before_invest - case['request_data']['amount'],
            user_balance_after_invest
        )  # 高精度的数据可以和整数运算，不能和浮点数运算
        # 标的的投资前可投资额 - 标的的投资后可投资额 =投资额
        self.assert_equal(
            bid_balance_before_invest - case['request_data']['amount'],
            bid_balance_after_invest
        )
        self.logger.info('********{}测试结束*********'.format(case['title']))

    #  注意：所有的判断要写在测试方法里

    def get_pop_error_tip(self):
        """
        获取弹出的错误提示信息（在标的的详情页）
        :return:
        """
        bp = BidPage(self.driver)
        return bp.get_pop_error_tip()

    def invest_success(self):
        """
        投资是否成功
        :return:
        """
        bp = BidPage(self.driver)
        if bp.get_success_invest_btn():
            return True
        return False