#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from base.api_recode import Recode


class APIResponse:
    code = Recode.OK.get_code()
    msg = Recode.OK.get_msg()
    data = {}

    def __init__(self, data, code: int = code, msg: str = msg):
        self.code = code
        self.msg = msg
        self.data = data

    def body(self):
        body = {
            'code': self.code,
            'msg': self.msg,
            'data': self.data
        }
        return body
