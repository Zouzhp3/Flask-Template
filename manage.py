#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
本文件是flask项目的启动脚本
常用命令包括：
1. python manage.py runserver  启动服务进程(单线程)
2. python manage.py db init/migrate/update  管理数据库
"""

import os
from APP import create_app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = create_app(os.getenv('APP_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
