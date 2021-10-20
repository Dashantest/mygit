#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/11 23:07
# @Author : 大山
import os
import time
from datetime import datetime

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import settings
from common.log_handler import logger


class BasePage:
    """
    页面对象的基类，封装常用操作（基本功能），节省代码量，便于维护
    1.查找元素  等待--查找--元素
    2.点击  等待--查找--点击
    3.输入  等待--查找--输入
    4.获取元素文本   等待--查找--获取元素文本
    5.获取元素属性   等待--查找--获取元素属性
    根据1-5的特点，先封装等待
    6.窗口切换
    7.失败截图
    """
    name = 'base页面'
    logger = logger
    settings = settings

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.element = None  # 绑定元素
        self.locator = None  # 绑定定位信息
        self.action = ''  # 绑定操作

    # 封装等待
    def wait_element_is_visible(self, locator, action='', **kwargs):
        """
        等待元素可见
        :param locator: 定位信息 tuple(by, expression)
        :param action: 操作说明 str
        :param kwargs: timeout 超时， pll_frequency 轮循的频率
        :return:
        """
        # 绑定
        self.locator = locator
        self.action = action
        # 初始化参数，如果有就用，没有就用配置文件默认的
        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            pll_frequency = kwargs.get('pll_frequency', 0.5)
            # 绑定element
            self.element = WebDriverWait(self.driver, timeout, pll_frequency).until(
                EC.visibility_of_element_located(locator)
            )
        except Exception as e:
            # 记录错误日志
            self.logger.exception(
                '在{}，{}操作的时候，等待{}元素可见【失败】'.format(self.name, action, locator)
            )
            # 生成错误截图
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素可见【成功】'.format(self.name, action, locator)
            )
            return self  # 返回self，方便链式编程

    def wait_element_to_be_clickable(self, locator, action='', **kwargs):
        """
        EC.element_to_be_clickable
        :param locator:
        :param action:
        :param kwargs:
        :return:
        """
        pass

    def wait_element_is_loaded(self, locator, action='', **kwargs):
        """
              等待元素加载到文档
              :param locator: 定位信息 tuple(by, expression)
              :param action: 操作说明 str
              :param kwargs: timeout 超时， pll_frequency 轮循的频率
              :return:
              """
        # 绑定
        self.locator = locator
        self.action = action
        # 初始化参数，如果有就用，没有就用配置文件默认的
        try:
            timeout = kwargs.get('timeout', self.settings.DEFAULT_TIMEOUT)
            pll_frequency = kwargs.get('pll_frequency', 0.5)
            # 绑定element
            self.element = WebDriverWait(self.driver, timeout, pll_frequency).until(
                EC.presence_of_element_located(locator)
            )
        except Exception as e:
            # 记录错误日志
            self.logger.exception(
                '在{}，{}操作的时候，等待{}元素加载到文档【失败】'.format(self.name, action, locator)
            )
            # 生成错误截图
            self.get_page_screenshot(action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，等待{}元素加载到文档【成功】'.format(self.name, action, locator)
            )
            return self  # 返回self，方便链式编程

    def get_element(self):
        """
        获取元素
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前，即未查到元素前，调用操作元素上的方法')
        return self.element

    # def click_element(self, locator, action=''):
    #     """
    #     搞不懂链式编程，就这么写，只是效率不高
    #     :param locator:
    #     :param action:
    #     :return:
    #     """
    #     try:
    #         self.driver.find_element(*locator).click()
    #     except Exception as e:
    #         self.logger.exception(
    #             '在{}，{}操作的时候，点击{}元素【失败】'.format(self.name, action, locator)
    #         )
    #         raise e
    #     else:
    #         self.logger.info(
    #             '在{}，{}操作的时候，点击{}元素【成功】'.format(self.name, action, locator)
    #         )

    def click_element(self):
        """
        点击元素
        :param locator:
        :param action:
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前，即未查到元素前，调用操作元素上的方法')
        try:
            self.element.click()
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，点击{}元素【失败】'.format(self.name, self.action, self.locator)
            )
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，点击{}元素【成功】'.format(self.name, self.action, self.locator)
            )
        finally:
            # 清空wait的缓存
            self.__clear_cache()

    def __clear_cache(self):
        """
        清空wait的缓存
        :return:
        """
        self.element = None
        self.locator = None
        self.action = ''

    def send_keys(self, content):
        """
        输入内容
        :param content: 输入数据
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前，即未查到元素前，调用操作元素上的方法')
        try:
            self.element.send_keys(content)
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，对{}元素输入{}【失败】'.format(self.name, self.action, self.locator, content)
            )
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，对{}元素输入{}【成功】'.format(self.name, self.action, self.locator, content)
            )
        finally:
            self.__clear_cache()

    def get_element_text(self):
        """
        获取元素的文本
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前，即未查到元素前，调用操作元素上的方法')
        try:
            text = self.element.text
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，获取{}元素的文本【失败】'.format(self.name, self.action, self.locator)
            )
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的文本【成功】'.format(self.name, self.action, self.locator)
            )
            return text
        finally:
            # 清空wait的缓存
            self.__clear_cache()

    def get_element_attr(self, name):
        """
        获取元素的属性
        :param name: 属性名称
        :return:
        """
        if self.element is None:
            raise RuntimeError('不能在wait前，即未查到元素前，调用操作元素上的方法')
        try:
            value = self.element.get_attribute(name)  # 获取元素
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，获取{}元素的{}属性【失败】'.format(self.name, self.action, self.locator, name)
            )
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，获取{}元素的{}属性【成功】'.format(self.name, self.action, self.locator, name)
            )
            return value
        finally:
            # 清空wait的缓存
            self.__clear_cache()

    def switch_to_new_window(self, handle=None, action=''):
        """
        切换到新的窗口
        :param handle:
        :param action:
        :return:
        """
        try:
            if handle:
                self.driver.switch_to.window(handle)
            else:
                # 获取当前默认的handle
                original_window = self.driver.current_window_handle
                # 循环当前所有窗口
                for handle in self.driver.window_handles:
                    if handle != original_window:
                        self.driver.switch_to.window(handle)
                        break
        except Exception as e:
            self.logger.exception(
                '在{}，{}操作的时候，切换到窗口{}【失败】'.format(self.name, self.action, handle)
            )
            self.get_page_screenshot(self.action)
            raise e
        else:
            self.logger.info(
                '在{}，{}操作的时候，切换到窗口{}【成功】'.format(self.name, self.action, handle)
            )

    def get_page_screenshot(self, action):
        """
        获取报错时的页面截图，命令规范XX页面XX操作_截图时间.png
        :param action:操作
        :return:
        """
        # 拼接截图路径
        img_path = os.path.join(self.settings.ERROR_SCREENSHOT_DIR, '{}_{}操作_{}.png'.format(
            self.name, action, datetime.now().strftime('%Y-%m-%d %H-%M-%S')
        ))  # datetime.now().strftime('%Y-%m-%d %H-%M-%S')获取当前时间，并格式化时间输出格式
        # 截图，路径一定要用绝对路径，后缀为.png
        if self.driver.save_screenshot(img_path):
            self.logger.info('生成错误截图：{}【成功】'.format(img_path))
        else:
            self.logger.error('生成错误截图：{}【失败】'.format(img_path))

    def delay(self, second=0.5):
        """
        延时操作
        :param second:单位秒，默认500毫秒，支持浮点数
        :return:
        """
        time.sleep(second)
        # 需要在两个方法之间调用延时，来实现链式编程，那么就必须返回self
        return self
