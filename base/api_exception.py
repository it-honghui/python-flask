#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask import json
from werkzeug.exceptions import HTTPException
from base.api_recode import Recode


class APIException(HTTPException):
    code = Recode.ERR.get_code()
    msg = Recode.ERR.get_msg()

    def __init__(self, code: int = None, msg: str = None):
        if code:
            self.code = code
        if msg:
            self.msg = msg

        super(APIException, self).__init__(msg, None)

    def get_body(self, environ=None):
        body = {
            'code': self.code,
            'msg': self.msg,
        }
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [('Content-Type', 'application/json')]
