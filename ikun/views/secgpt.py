#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : yds
# @Time    : 18-5-17
# @File    : secgpt.py
# @Desc    : SecGPT 页面注册

from flask import Blueprint, render_template

# 创建 secgpt 蓝图
secgpt = Blueprint('secgpt', __name__)

# 注册路由
@secgpt.route('/secgpt', methods=['GET'])
def secgpt_view():
    # 渲染 HTML 页面
    return render_template('secgpt.html')
