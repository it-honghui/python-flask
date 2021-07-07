#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from domain.base.vo_base_model import VoBaseModel


class Book(VoBaseModel):
    def __init__(self, _id: int, name: str, price: str):
        self.id = _id
        self.name = name
        self.price = price

    def __str__(self):
        return 'id:%s name:%s price:%s' % (self.id, self.name, self.price)
