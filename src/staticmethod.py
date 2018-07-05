#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/5 下午4:09
# @Author  : Aries (i@iw3c.com)
# @Site    : http://iw3c.com
# @File    : staticmethod.py
# @Software: PyCharm

class Sunmoon():

    age = 19

    def __init__(self):
        self.age = 18

    @staticmethod
    def myName():
        print('My name is sunmoon')

    @classmethod
    def myAge(sun):
        print(sun.age)

    def realAge(self):
        print(self.age)

if __name__ == '__main__':
    Sunmoon.myName()
    Sunmoon.myAge()
    s = Sunmoon()
    s.realAge()