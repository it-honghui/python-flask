#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask import jsonify
from functools import wraps
from base.api_response import APIResponse


def route(bp, *args, **kwargs):
    def decorator(f):
        @bp.route(*args, **kwargs)
        @wraps(f)
        def wrapper(*_args, **_kwargs):
            result = f(*_args, **_kwargs)
            res = APIResponse(result)

            return jsonify(res.body())

        return f

    return decorator
