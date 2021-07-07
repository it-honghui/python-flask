#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from base import app
from app import healthy, user, book

app.register_blueprint(healthy.bp, url_prefix='/')
app.register_blueprint(user.bp, url_prefix='/user')
app.register_blueprint(book.bp, url_prefix='/book')
