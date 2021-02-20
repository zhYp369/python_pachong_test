#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
@project: python_pachong_jindong_test
@file: viems
@time: 2021/2/20/020 14:56
@author: Administrator
@desc: 
"""

from flask import Blueprint
from flask import render_template

blue = Blueprint("viems", __name__)


@blue.route('/home/', methods=['GET'])
def home():
    return "hello"



import time  # 引入time模块

ticks = time.time()
print ("当前时间戳为:", ticks)