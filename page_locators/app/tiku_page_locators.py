#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 23:34
# @Author : 大山
from appium.webdriver.common.mobileby import MobileBy



class TiKuPageLocators:
    # ===================题库首页=======================
    # 每个题库的定位
    tk_title_loc = ('xpath', '//*[@resource-id="com.lemon.lemonban:id/fragment_category_type"]')
    # ===================题库详情页=====================
    # 题号的定位
    question_num_loc = (MobileBy.ID, 'com.lemon.lemonban:id/toolbar_textview')
    # 点击查看题目答案
    answer_btn_loc = (MobileBy.ID, 'com.lemon.lemonban:id/switch_button')
    # 获取题目答案
    answer_text_loc = (MobileBy.ID, 'com.lemon.lemonban:id/tvBody')