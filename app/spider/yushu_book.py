#!/usr/bin/python
#coding: utf8

from app.libs.http import HTTP
from flask import current_app

class YuShuBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    @classmethod
    def search_by_isdn(cls,isbn):
        url = cls.isbn_url.format(isbn)
        result = HTTP.get(url)
        return result

    @classmethod
    def search_by_keyword(cls,keyword,page=1):
        url = cls.keyword_url.format(keyword,current_app.config['PER_PAGE'],cls.caculated_count(page))
        result = HTTP.get(url)
        return result

    @staticmethod
    def caculated_count(page):
        return (page-1)*current_app.config['PER_PAGE']
