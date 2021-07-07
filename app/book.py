#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: Honghui <wanghonghui_work@163.com> 2021/07/07
# Desc:

from flask import Blueprint, request
from base.api_route import route
from domain.book import Book
from base.api_exception import APIException
from base.api_recode import Recode

bp = Blueprint('book', __name__)


# find lists
@route(bp, '/', methods=['GET'])
def find_books():
    # a = 10 / 0
    # raise APIException(Recode.NOT_FOUND.get_code(), Recode.NOT_FOUND.get_msg())
    return [
        Book(1, name='西游记', price='11.11'),
        Book(2, name='水浒传', price='22.22'),
        Book(3, name='红楼梦', price='33.33')
    ]


# find by id
@route(bp, '/<book_id>', methods=['GET'])
def find_book(book_id):
    return Book(book_id, name='西游记', price='11.11')


# find props
@route(bp, '/<book_id>/name', methods=['GET'])
def find_book_name(book_id):
    return '西游记'


# find by props
@route(bp, '/_search', methods=['GET'])
def search():
    name = request.args.get("name")
    return [
        Book(1, name=name, price='11.11'),
        Book(2, name=name, price='22.22'),
        Book(3, name=name, price='33.33')
    ]


# batch find by props
@route(bp, '/_search', methods=['POST'])
def search2():
    data = request.json
    id_list = data.get('id')
    books = []
    for book_id in id_list:
        books.append(Book(book_id, name='西游记', price='11.11'))
    return books


# create(always create new one)
@route(bp, '/', methods=['POST'])
def create():
    return request.json


# create / overwrite
@route(bp, '/', methods=['PUT'])
def save():
    return request.json


# delete by id
@route(bp, '/<book_id>', methods=['DELETE'])
def delete(book_id):
    return '删除成功:' + book_id


# change prop
@route(bp, '/<book_id>', methods=['PATCH'])
def patch(book_id):
    name = request.form.get("name")
    return Book(book_id, name=name, price='11.11')
