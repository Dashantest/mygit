#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 23:34
# @Author : 大山
from page_objects.app.app_base_page import AppBasePage
from page_locators.app.tiku_page_locators import TiKuPageLocators



class TiKuPage(AppBasePage):
    name = '题库页面'

    def select_ti_ku_by_name(self, name):
        """
        根据题库名字进入指定题库
        :param name:
        :return:
        """
        action = '进入{}题库'.format(name)
        # 根据输入的名字模糊匹配
        loc = ('xpath', '//*[contains(@text,"{}")]'.format(name))
        # 显示所有的题库
        ts = []
        while True:
            try:
                # 找题库
                self.wait_element_is_visible(loc, action, timeout=3).click_element()
            except Exception as e:
                # 找出当前显示的所有题库，并按顺序添加到列表
                qs = self.driver.find_elements(*TiKuPageLocators.tk_title_loc)
                temp = [e.text for e in qs]   # 列表生成式，等价于下面的代码
                # temp = []
                # for item in qs:
                #     temp.append(item.text)
                # print(temp)
                # ts == temp时，说明已经滑到底部
                if ts == temp:
                    self.logger.warning('没有{}这个题库'.format(name))
                    raise ValueError('没有{}这个题库'.format(name))
                # ts != temp就将temp赋值给ts
                ts = temp
                # 2. 找不到就滑动
                self.swipe('up', 500)
                self.delay(1)
            else:
                break

    def select_level_by_name(self, level_name):
        """
        根据等级名称选择对应等级
        :param level_name:
        :return:
        """
        loc = ('xpath', '//*[@text="{}"]'.format(level_name))
        action = '选择{}'.format(level_name)
        self.wait_element_is_visible(loc, action).click_element()

    def select_set_by_name(self, set_name):
        """
        根据套名选择对应的套题
        :param set_name:
        :return:
        """
        loc = ('xpath', '//*[contains(@text, "{}")]'.format(set_name))
        action = '选择{}'.format(set_name)
        self.wait_element_is_visible(loc, action).click_element()

    def select_question_by_num(self, num):
        """
        根据题目序号选择题目
        :param num:传入的需要测试的题号
        :return:
        """
        while True:
            q_num = self.wait_element_is_visible(
                TiKuPageLocators.question_num_loc, '选择题目时获取题号').get_element_text()
            q_num, t_num = q_num.split('/') # q_num 当前题号 t_num 总题数，均为str然后int
            q_num = int(q_num)
            t_num = int(t_num)
            if num > t_num:
                raise ValueError('超过题目的最大序号')
            if num > q_num:
                self.swipe('left', 500)
            elif num < q_num:
                self.swipe('right', 500)
            else:
                break

    def get_answer(self):
        self.wait_element_is_visible(TiKuPageLocators.answer_btn_loc, '点击查看题目答案').click_element()
        try:
            answer = self.wait_element_is_visible(
                TiKuPageLocators.answer_text_loc, '获取题目答案').get_element_text()
        except Exception as e:
            pass
        else:
            return answer