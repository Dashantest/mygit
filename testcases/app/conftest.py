#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：conftest.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:49
import pytest

from appium import webdriver

import settings
from page_objects.app.navigation_page import NavigationPage
from page_objects.app.my_page import MyPage
from page_objects.app.login_page import LoginPage


@pytest.fixture(scope='class')
def driver():
    with webdriver.Remote(settings.APPIUM_SERVER_HOST, desired_capabilities=settings.DESIRED_CAPS) as session:
        yield session


# 登录用例前置条件，我的柠檬页面
@pytest.fixture(scope='class')
def to_my_page_driver(driver):
    """
    进入我的页面
    :param driver:
    :return:
    """
    np = NavigationPage(driver)
    np.switch_navigation('我的柠檬')
    yield driver


@pytest.fixture(scope='class')
def signed_in_driver(to_my_page_driver):
    """
    已登录的前置条件
    :param to_my_page_driver:
    :return:
    """
    # 点击我的头像，进入登录页面
    mp = MyPage(to_my_page_driver)
    mp.enter_login_page()
    # 登录
    lp = LoginPage(to_my_page_driver)
    lp.login(**settings.TEST_USER)
    yield to_my_page_driver
