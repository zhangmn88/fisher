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
            returnd['book'] = [cls.__cut_book_data(data)]
        return returnd

    def package_collection(self,data,keyword):
        pass

    @classmethod
    def __cut_book_data(cls,data):
        book = {
            'title':data['title'],
            'publisher':data['publiser'],
            'author':'、'.join(data['author']),
            'pages':data['pages'],
            'price':data['price'],
            'summary':data['summary'],
            'image':data['image']
        }
        return book
