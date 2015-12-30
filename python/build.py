#!/usr/bin/python
# -*- coding: utf-8 -*-

# 读取文本文件生成指定格式的json文件

import sys
import os

class crac:
    def __init__(self):
        pass
    def init(self):
        reload(sys)
        sys.setdefaultencoding('utf-8')
    def readFile(self, path):
        f = open(path, 'rb')
        lines = f.readlines()
        print lines[111].strip()
    def run(self):
        print "run"

def main():
    c = crac()
    c.init()
    c.readFile(u'../files/总题库文件(v150612).txt')

if __name__=='__main__':
    main()