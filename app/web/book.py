#!/usr/bin/python
#coding: utf8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from flask import jsonify,request
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.books import SearchForm


@web.route('/book/search/')
def index():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isdn':
            result = YuShuBook.search_by_isdn(q)
        else:
            result = YuShuBook.search_by_keyword(q,page)

        # dict序列化
        return jsonify(result)

    return jsonify(form.errors)