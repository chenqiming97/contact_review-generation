#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/11/10 14:05
@Author     : jzs
@File       : index.py
@Software   : PyCharm
@Description: 主目录路由
"""

from flask import render_template, request, flash, current_app, redirect, url_for
from flask_login import login_required, login_user

# 初始化蓝图命名空间index_bp
from flask_principal import identity_changed, Identity

# from app.models.cont_gen_element_table import ContGenElementTable
# from app.models.contract_gen_table import ContractGenTable
from app.models.user import User
from . import mainBlueprint


# 根目录
@mainBlueprint.route('/')
def index():
    return render_template('login.html')


# 后台登陆-->登陆验证
@mainBlueprint.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.get_one_user(username, password)
        if username == '':
            flash('请输入用户名')
            return render_template('login.html')
        elif password == '':
            flash('请输入密码')
            return render_template('login.html')
        elif user is not None:
            login_user(user, remember=True)
            identity_changed.send(current_app._get_current_object(), identity=Identity(user.user_id))
            return redirect(url_for('main.pagecs'))
        else:
            flash('用户名或密码不正确')
            return render_template('login.html')


# 日志信息登录
@mainBlueprint.route('/admin_log_first', methods=['POST', 'GET'])
@login_required
def admin_log_first():
    """
    日志信息登录
    :return:
    """
    pass


@mainBlueprint.route('/pagecs', methods=['POST', 'GET'])
@login_required
def pagecs():
    """
    合同页面选择
    :return:
    """
    return render_template('pagechoose.html')


@mainBlueprint.route('/admin_index', methods=['POST', 'GET'])
@login_required
def admin_index():
    """
    后台首页
    :return:
    """
    return render_template('admin_index.html')
