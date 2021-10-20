#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/7 22:55
# @Author : 大山
import settings
from common.log_handler import logger


class BaseCase:
    """
    测试用例基类
    """
    name = None
    logger = logger
    settings = settings

    # 使用xunit风格的前置后置
    @classmethod
    def setup_class(cls):
        cls.logger.info('***********{}开始测试**********'.format(cls.name))

    @classmethod
    def teardown_class(cls):
        cls.logger.info('***********{}测试结束**********'.format(cls.name))

    # 封装断言，然后调用，当断言有修改直接修改自己封装的
    # def my_assert(self, check_data, title='XX测试'):
    #     """
    #     断言
    #     :param check_data:
    #     :param title:用例标题
    #     :return:
    #     """
    #     try:
    #         method = getattr(self, check_data['method'])
    #         assert method() == check_data['value']
    #     except Exception as e:
    #         self.logger.exception('{}测试失败'.format(title))
    #         raise e
    #     else:
    #         self.logger.info('{}测试成功'.format(title))

    def my_assert(self, check_data, title='XX测试'):
        """
        断言
        :param check_data:
        :param title:用例标题
        :return:
        """
        method = getattr(self, check_data['method'])
        res = method()
        try:
            # 调用自己封装的断言是否相等的方法
            self.assert_equal(res, check_data['value'])
        except Exception as e:
            self.logger.warning('测试函数返回的实际结果是：{}'.format(res))
            self.logger.warning('期望结果是：{}'.format(check_data['value']))
            self.logger.exception('{}测试失败'.format(title))
            raise e
        else:
            self.logger.info('{}测试成功'.format(title))

    def assert_equal(self, first, second, msg=''):
        """
        断言相等
        :param first:
        :param second:
        :param msg:
        :return:
        """
        if first != second:
            if msg:
                raise AssertionError(msg)
            else:
                raise AssertionError('{} != {}'.format(first, second))
