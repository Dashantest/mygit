#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 22:29
# @Author : 大山
import pytest
from selenium import webdriver

import settings
from page_objects.web.login_page import LoginPage

# 夹具的范围根据业务的实际情况来决定
@pytest.fixture(scope='class')
def driver():
    with webdriver.Chrome() as wb:
        # 最大化浏览器
        wb.maximize_window()
        print('我是driver夹具')
        yield wb

# @pytest.fixture(scope='class')
# def login_driver():
#     with webdriver.Chrome() as wb:
#         # 最大化浏览器
#         wb.maximize_window()
#         lp = LoginPage(wb)
#         lp.login(settings.TEST_NORMAL_USERNAME, settings.TEST_NORMAL_PASSWORD)

# 继承夹具的范围要<=被继承夹具的范围
@pytest.fixture(scope='class')
def login_driver(driver):
    """
    继承了上面的driver
    :param driver:
    :return:
    """
    lp = LoginPage(driver)
    lp.login(settings.TEST_NORMAL_USERNAME, settings.TEST_NORMAL_PASSWORD)
    yield driver