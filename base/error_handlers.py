#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from base import app
from base.api_exception import APIException
from base.api_recode import Recode
import traceback


@app.errorhandler(Exception)
def framework_error(e):
    code = Recode.ERR.get_code()
    msg = str(e)
    if isinstance(e, APIException):
        code = e.code
        msg = e.msg
    app.logger.error(traceback.format_exc())
    return APIException(code=code, msg=msg)
