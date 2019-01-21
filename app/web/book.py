#!/usr/bin/python
#coding: utf8

import sys

from flask import jsonify,request
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.books import SearchForm
from app.view_models.book import BookViewModel

reload(sys)
sys.setdefaultencoding('utf8')


@web.route('/book/search/')
def index():
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isdn':
            result = YuShuBook.search_by_isdn(q)
            result = BookViewModel.package_single(result,q)
        else:
            result = YuShuBook.search_by_keyword(q,page)
            result = BookViewModel.package_collection(result,q)

        # dict序列化
        return jsonify(result)

    return jsonify(form.errors)