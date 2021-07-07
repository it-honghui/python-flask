#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask import Blueprint
from base.api_route import route

bp = Blueprint('healthy', __name__)


@route(bp, '/')
def healthy():
    return 'healthy'
