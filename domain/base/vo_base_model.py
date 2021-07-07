#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:


class VoBaseModel:
    __abstract__ = True

    @staticmethod
    def vo_to_dict(obj):
        res = {}
        for name in dir(obj):
            value = getattr(obj, name)
            if not name.startswith('__') and not callable(value):
                res[name] = value
        return res
