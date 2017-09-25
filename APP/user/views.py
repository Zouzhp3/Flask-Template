#! /usr/bin/env python
# -*- coding: utf-8 -*-
from flask import render_template, redirect, request, url_for, current_app, abort, jsonify, session
from flask_login import login_user, logout_user, current_user, login_required
from datetime import datetime
from flask_babel import gettext
from . import user
from ..models import User
from .. import db
import os


@user.route('/register/', methods=['GET', 'POST'])
def reg():
    pass


@user.route('/login/', methods=['GET', 'POST'])
def login():
    pass
