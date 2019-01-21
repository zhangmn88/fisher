#!/usr/bin/python
#coding: utf8

class BookViewModel(object):
    @classmethod
    def package_single(cls,data,keyword):
        returnd = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returnd['total'] = 1
            returnd['books'] = [cls.__cut_book_data(data)]
        return returnd

    @classmethod
    def package_collection(cls,data,keyword):
        returnd = {
            'books':[],
            'total':0,
            'keyword':keyword
        }
        if data:
            returnd['total'] = data['total']
            returnd['books'] = [cls.__cut_book_data(data) for data in data['books']]
        return returnd

    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publisher'],
            'author':'、'.join(data['author']),
            'pages':data['pages'] or '',
            'price':data['price'],
            'summary':data['summary'] or '',
            'image':data['image']
        }
        return book
