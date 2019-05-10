#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/11/10 11:03
@Author     : jzs
@File       : __init__.py.py
@Software   : PyCharm
@Description: 初始化蓝图
"""
from flask import Flask
from flask import Blueprint

mainBlueprint = Blueprint('main', __name__)

from . import errors,admin,contract_generate,suggestion,contract_review,sign
# 配置蓝图的对象以及蓝图的VIEWS的访问路径
DEFAULT_BLUEPRINT = (
    (mainBlueprint, '')
)


def config_blueprint(app: 'Flask'):
    """
    封装配置蓝本的函数，循环读取元组中的蓝本，注册蓝本对象
    :param app: Flask app对象
    :return:
    """
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
