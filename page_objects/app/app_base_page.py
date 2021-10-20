#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Project ：auto_test_interface 
# File    ：app_base_page.py
# IDE     ：PyCharm 
# Author  ：Runner
# Date    ：2021/1/25 14:50
from page_objects.base_page import BasePage


class AppBasePage(BasePage):
    name = 'app base 页面'

    def get_device_size(self):
        """
        获取设备屏幕大小
        :return:
        """
        size = self.driver.get_window_size()
        return size['width'], size['height']

    def get_toast_msg(self):
        """
        获取toast信息
        :return:
        """
        # 获取toast作信息
        toast_msg_loc = ('xpath', '//*[@class="android.widget.Toast"]')
        action = '获取toast信息'
        msg = None
        # msg先加一个占位符，如果定位出错，报错就return  None，否则return   msg
        try:
            # toast信息的display属性永远是false，所以等待条件不要用可见
            msg = self.wait_element_is_loaded(toast_msg_loc, action).get_element_text()
        except Exception as e:
            pass
        else:
            return msg

    def swipe(self, direction, distance=100):
        """
        页面滑动
        :param direction:方向
        :param distance:距离，默认滑动100
        :return:
        """
        width,height = self.get_device_size()
        if direction == 'up':
            start_x = width // 2
            start_y = height * 8 // 10  # 这样计算方便取整好计算
            end_x = start_x
            end_y = start_y - distance
        elif direction == 'down':
            start_x = width // 2
            start_y = height * 2 // 10
            end_x = start_x
            end_y = start_y + distance
        elif direction == 'left':
            start_x = width * 8 // 10
            start_y = height // 2
            end_x = start_x -distance
            end_y = start_y
        elif direction == 'right':
            start_x = width * 2 // 10
            start_y = height // 2
            end_x = start_x -distance
            end_y = start_y
        else:
            raise ValueError('请传入一下正确的方向字符串参数，up,down,left,right')
        self.driver.swipe(start_x, start_y, end_x, end_y, 500) # 实际调用driver的swipe()方法，延时500