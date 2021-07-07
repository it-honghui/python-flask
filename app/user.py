#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask import Blueprint
from base.api_route import route
from domain.user import User

bp = Blueprint('user', __name__)


@route(bp, '/')
def user():
    users = User.query.all()
    return users
