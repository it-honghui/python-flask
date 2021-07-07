#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

import logging
import environment
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.%s.Config' % environment.ENV)
db = SQLAlchemy(app)

from base import error_handlers
from base.json_encoder import JSONEncoder

app.json_encoder = JSONEncoder

handler = logging.FileHandler('%s/flask.log' % app.config['LOG_PATH'])
logging.root.setLevel(app.config['LOG_LEVEL'])
app.logger.addHandler(handler)
