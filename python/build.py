#!/usr/bin/python
# -*- coding: utf-8 -*-

# 读取文本文件生成指定格式的json文件

import sys
import os

ALL_EXAM_FILE = u'../files/总题库文件(v150612).txt'
A_INDEX = u'../files/A_试卷涉及题号(v150612).txt'
B_INDEX = u'../files/B_试卷涉及题号(v150612).txt'
C_INDEX = u'../files/C_试卷涉及题号(v150612).txt'
IMG_PATH = u'../files/总题库附图(v140331)'

A_NUM = 30
B_NUM = 50
C_NUM = 80

#########################################################

class my_question:
    def __init__(self):
        self.index = u''
        self.question = u''
        self.answers = []
        self.image = u''
    def get_json(self):
        return {}
    def is_finished(self):
        return True

class line_processer:
    def __init__(self):
        self.line
    def process(self, line):
        self.line = line.strip()
    def is_empty(self, line):
        return self.line == ''
    def is_index(self, line):
        return self.line.startswith("[I]")
    def is_question(self, line):
        return self.line.startswith("[Q]")
    def is_right_answer(self, line):
        return self.line.startswith("[A]")
    def is_last_answer(self, line):
        return self.line.startswith("[I]")
    def is_image_need(self, line):
        return self.line.startswith("[P]")

class builder:
    def __init__(self):
        self.raw_questions_lines = []
        self.raw_a_indexs = []
        self.raw_b_indexs = []
        self.raw_c_indexs = []

        self.a_indexs = []
        self.b_indexs = []
        self.c_indexs = []

        reload(sys)
        sys.setdefaultencoding('utf-8')

    def readFiles(self):
        self.raw_questions_lines = self.readFileLines(ALL_EXAM_FILE)
        self.raw_a_indexs = self.readFileLines(A_INDEX)
        self.raw_b_indexs = self.readFileLines(B_INDEX)
        self.raw_c_indexs = self.readFileLines(C_INDEX)

    def readFileLines(self, path):
        rst = []
        f = open(path, 'rb')
        for l in f.readlines():
            rst.append(l.strip())
        f.close()
        return rst

    def run(self):
        self.readFiles()
        print len(self.raw_questions_lines)
        self.a_indexs = self.process_indexs(self.raw_a_indexs[0])
        print "A level: %d, %d, %s" % (len(self.raw_a_indexs), len(self.a_indexs), self.a_indexs)
        self.b_indexs = self.process_indexs(self.raw_b_indexs[0])
        print "B level: %d, %d" % (len(self.raw_b_indexs), len(self.b_indexs))
        self.c_indexs = self.process_indexs(self.raw_c_indexs[0])
        print "C level: %d, %d" % (len(self.raw_c_indexs), len(self.c_indexs))

    def process_indexs(self, idxs):
        rst = []
        for _ in idxs.split(' '):
            # print _.strip()[0:6]
            rst.append(_.strip()[0:6])
        return rst

def main():
    b = builder()
    b.run()

if __name__=='__main__':
    main()