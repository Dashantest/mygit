#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 20:37
# @Author : 大山
weight = float(input('请输入你的体重（kg）：'))
height = float(input('请输入你的身高（m）：'))
bmi = weight/(height**2)
if 0<bmi<18.5:
    print("偏瘦，国际BMI值为<18.5，国内BMI值为<18.5")
elif 18.5<=bmi<=25:
    pass