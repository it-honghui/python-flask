#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:
from base import db
from domain.base.db_base_model import DbBaseModel


class User(DbBaseModel):
    __tablename__ = 'user'

    id = db.Column(db.BigInteger, primary_key=True, info='主键自增')
    username = db.Column(db.String(32), nullable=False, unique=True, info='用户名')
    password = db.Column(db.String(64), nullable=False, info='密码')
