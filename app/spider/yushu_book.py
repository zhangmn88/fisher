#!/usr/bin/python
# coding: utf8


from app.libs.http import HTTP
from flask import current_app

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class YuShuBook(object):
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isdn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        if data:
            self.total = data['total']
            self.books = data['books']

    def search_by_keyword(self, keyword, page=1):
        url = self.keyword_url.format(keyword,current_app.config['PER_PAGE'],self.caculated_count(page))
        result = HTTP.get(url)
        self.__fill_collection(result)

    def caculated_count(self, page):
        return (page-1)*current_app.config['PER_PAGE']
