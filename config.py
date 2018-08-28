#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
config.py 是初始化 Flask app 的配置文件,当创建一个 app 时,将选择一种配置进行初始化
项目用到的全局变量也写在这个文件中
主要包括多种模式下的配置类型和全局参数（如密钥、连接数据库的 URL） 等

config.py、APP/init.py 以及 manage.py 之间的关系：
1. config.py 是创建app时需参考的配置文件,即使用何种配置（生产环境或开发环境）
2. APP/init.py 是创建app的具体工厂函数，并包括了路由的配置。该文件使用了config.py中的配置。
3. manage.py 是创建以及运行app的一个通用脚本，该文件使用了 APP/init.py
"""

import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    def __init__(self):
        pass

    # 此处定义全局变量
    SECRET_KEY = os.environ.get('SECRET_KEY') or '!@#$%^&*12345678'  # 设置密钥，可能会用在某些涉及到加解密的功能中
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # 该项不设置为True的话可能会导致数据库报错

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
    DEBUG = True         # 调试模式：热更新
    ENV = 'development'  # 环境配置项，默认为'production'

    SQLALCHEMY_DATABASE_URI = (os.environ.get('DEV_DATABASE_URL') or
                               'mysql+pymysql://root:123456@localhost/app_dev')  # 连接测试环境数据库的URL


class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
    DEBUG = False
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = (os.environ.get('PRO_DATABASE_URL') or
                               'mysql+pymysql://root:123456@localhost/app_pro')  # 连接生产环境数据库的URL


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
