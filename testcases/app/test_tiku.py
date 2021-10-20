#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 23:17
# @Author : 大山
import pytest

from testcases.base_test_case import BaseCase
from testdata.app.tiku_data import test_data
from page_objects.app.navigation_page import NavigationPage
from page_objects.app.tiku_page import TiKuPage


class TestTiKu(BaseCase):
    name = '题库'

    @pytest.mark.parametrize('case', test_data)
    def test_tiku(self,signed_in_driver, case):
        # 1.进入题库页面
        np = NavigationPage(signed_in_driver)
        np.switch_navigation('题库')
        # 2.进入对应题库
        tp = TiKuPage(signed_in_driver)
        tp.select_ti_ku_by_name(case['name'])
        # 3.进入对应等级
        tp.select_level_by_name(case['level'])
        # 4.进入对应套题
        tp.select_set_by_name(case['set_num'])
        # 5.进入对应题目
        tp.select_question_by_num(case['question_num'])
        # 6.打开答案
        answer = tp.get_answer()
        if not answer:
            raise AssertionError('{}测试失败'.format(case['title']))