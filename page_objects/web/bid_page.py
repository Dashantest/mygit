#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/13 22:36
# @Author : 大山
from decimal import Decimal

from page_objects.base_page import BasePage
from page_locators.web.bid_page_locators import BidPageLocators as BPloc


class BidPage(BasePage):
    name = '标的详情页'

    def invest(self, amount):
        """
        投资
        :param amount: 金额
        :return:
        """
        # 1. 输入投资金额
        self.wait_element_is_visible(BPloc.invest_input_loc, '输入投资金额').send_keys(amount)
        # 2. 点击【投资】
        self.wait_element_is_visible(BPloc.invest_btn, '点击【投标】').click_element()

    def get_pop_error_tip(self):
        """
        获取弹框的错误信息
        :return:
        """
        return self.wait_element_is_visible(BPloc.error_tip_loc, '获取弹框错误提示信息').get_element_text()

    def get_user_balance(self):
        """
        获取用户余额
        :return:
        """
        # balance  是一个浮点数字符串，需要转换成高精度
        balance = self.wait_element_is_visible(BPloc.invest_input_loc, '获取用户余额').get_element_attr('data-amount')
        return Decimal(balance)

    def get_bid_balance(self):
        """
        获取标的可投资额
        :return:
        """
        balance = self.wait_element_is_visible(BPloc.invest_input_loc, '获取标的可投资额').get_element_attr('data-left')
        return Decimal(balance)

    def get_success_invest_btn(self):
        """
        获取投资成功弹框的标识
        :return:
        """
        try:
            self.wait_element_is_visible(BPloc.success_pop_btn_loc, '获取投资成功弹框的标识').get_element()
        except:
            pass
        else:
            return True
        return False