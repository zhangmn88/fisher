#!/usr/bin/python
#coding: utf8

#判断是isbn还是书名
def is_isbn_or_key(word):
    is_isbn_or_key = 'key'

    if len(word) == 13 and word.isdigit():
        is_isbn_or_key = 'isdn'

    short_word = word.replace('-','')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        is_isbn_or_key = 'isdn'

    return is_isbn_or_key

