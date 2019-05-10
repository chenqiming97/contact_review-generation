#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@Time       : 2018/11/10 13:46
@Author     : jzs
@File       : Config.py
@Software   : PyCharm
@Description: 项目配置文件
"""
import os

# 项目的基础路径
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    定义配置基类
    """
    BOOTSTRAP_SERVE_LOCAL = True

    # 设置session的保存时间为7天
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)

    # 秘钥
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'

    # 数据库AES加密密钥
    db_str_key = "jcjjzgzzgsgss"

    # 数据库公用配置
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_POOL_SIZE = 100
    SQLALCHEMY_POOL_RECYCLE = 2

    # 上传文件路径
    UPLOADED_DIR_PATH = os.path.join(BASE_DIR, 'app/static/uploads')

    # 合同模板生成的路径
    CONT_GENA_TEMPLATE_DIR_PATH = os.path.join(BASE_DIR, 'app/static/docx/template')

    # 合同流转单目录模板路径
    CONT_FLOW_TABLE_DIR_PATH = os.path.join(BASE_DIR, 'app/static/docx/docx_ft')

    # 合同生成结构的目录路径
    CONT_GENA_DIR_PATH = os.path.join(BASE_DIR, 'app/static/docx/docx_repo')

    # 日志文件路径
    LOG_FILE_PATH = os.path.join(BASE_DIR, 'flask_log.log')

    # 机器学习和深度学习模型文件的路径
    STATIC_ELEM_MODEL= os.path.join(BASE_DIR, 'app/static/elem_model')

    # 额外的初始化操作
    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    """
    开发环境配置
    """
    DEBUG = True
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1:3306/css2?charset=utf8mb4&autocommit=true'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/css2?charset=utf8mb4&autocommit=true'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/css2?charset=utf8mb4&autocommit=true'


class TestingConfig(Config):
    """
    测试环境配置
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/css2?charset=utf8mb4&autocommit=true'


class ProductionConfig(Config):
    """
    生产环境配置
    """
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@localhost:3306/css2?charset=utf8mb4&autocommit=true'


# 生成一个字典，用来根据字符串找到对应的配置类
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
