#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from base import db


class DbBaseModel(db.Model):
    __abstract__ = True

    @staticmethod
    def db_to_dict(obj):
        res = {}
        for c in obj.__table__.columns:
            value = getattr(obj, c.name, '')
            res[c.name] = value
        return res
