#!/usr/bin/python
# coding: utf8

import json
import sys

from flask import jsonify, request, render_template
from . import web
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.forms.books import SearchForm
from app.view_models.book import BookViewModel, BookCollection

reload(sys)
sys.setdefaultencoding('utf8')


@web.route('/book/search/')
def index():
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isdn':
            yushu_book.search_by_isdn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book,q)
        # dict序列化
        return json.dumps(books, default=lambda o: o.__dict__, ensure_ascii=False)
        # return jsonify(books)

    return jsonify(form.errors)


@web.route('/test/')
def test():
    data = {
        'name': 'zxg',
        'age': 18
    }
    return render_template('test.html',data=data)