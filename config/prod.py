#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

import logging


class Config:
    LOG_PATH = './log'
    LOG_LEVEL = logging.INFO

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
