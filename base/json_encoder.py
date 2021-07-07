#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask.json import JSONEncoder as BaseJSONEncoder
import datetime
import decimal

from domain.base.db_base_model import DbBaseModel
from domain.base.vo_base_model import VoBaseModel


class JSONEncoder(BaseJSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return o.strftime('%Y-%m-%d %H-%M-%S')
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, DbBaseModel):
            return o.db_to_dict(o)
        if isinstance(o, VoBaseModel):
            return o.vo_to_dict(o)
        return super(JSONEncoder, self).default(o)
