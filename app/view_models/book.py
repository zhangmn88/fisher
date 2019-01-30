#!/usr/bin/python
# coding: utf8

# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')


class BookViewModel(object):
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = book['author']
        self.pages = book['pages']
        self.price = book['price']
        self.summary = book['summary']
        self.image = book['image']


class BookCollection(object):
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]


class _BookViewModel(object):
    @classmethod
    def package_single(cls, data, keyword):
        returnd = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returnd['total'] = 1
            returnd['books'] = [cls.__cut_book_data(data)]
        return returnd

    @classmethod
    def package_collection(cls, data, keyword):
        returnd = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            returnd['total'] = data['total']
            returnd['books'] = [cls.__cut_book_data(data) for data in data['books']]
        return returnd

    @classmethod
    def __cut_book_data(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'author': '、'.join(data['author']),
            'pages': data['pages'] or '',
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
