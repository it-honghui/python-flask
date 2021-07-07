#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

import requests


def get(url, params: dict = None, headers: dict = None):
    if headers is None:
        headers = {}
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    return requests.get(url, params=params, headers=headers)


def post_form(url, data=None, headers: dict = None):
    if headers is None:
        headers = {}
    headers['Content-Type'] = "application/x-www-form-urlencoded; charset=UTF-8"
    return requests.post(url, data=data, headers=headers)


def post_json(url, data=None, headers: dict = None):
    if headers is None:
        headers = {}
    headers['Content-Type'] = "application/json; charset=UTF-8"
    return requests.post(url, data=data, headers=headers)
