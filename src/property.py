#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午4:17
# @Author  : Aries (i@iw3c.com)
# @Site    : http://iw3c.com
# @File    : property.py
# @Software: PyCharm

class Person:
    __score = 10
    def __init__(self):
        self.__score = 20

    def score(self):
        return self.__score

if __name__ == '__main__':
    p = Person()
    print(p.score())