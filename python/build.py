#!/usr/bin/python
# -*- coding: utf-8 -*-

# 读取文本文件生成指定格式的json文件

import sys
import os
import copy
import json

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
        self.line = u''
        self.q = {}
    def process(self, line):
        self.line = line.strip()
        if self.is_index():
            temp = None
            if self.q == {}:
                self.q = {"index": self.clean_head(self.line), "answers": []}
                return temp
            else:
                temp = copy.deepcopy(self.q)
                self.q = {"index": self.clean_head(self.line), "answers": []}
            return temp
        elif self.is_empty():
            return None
        elif self.is_question():
            self.q["question"] = self.clean_head(self.line)
            return None
        elif self.is_answer():
            self.q["answers"].append(self.clean_head(self.line))
        elif self.is_image_need():
            self.q["image"] = self.clean_head(self.line)
        else:
            return None
    def get_last(self):
        return self.q
    def clean_head(self, line):
        return line[3:]
    def is_empty(self):
        return self.line == ''
    def is_index(self):
        return self.line.startswith("[I]")
    def is_question(self):
        return self.line.startswith("[Q]")
    def is_answer(self):
        return self.line.startswith("[A]") or self.line.startswith("[B]") or self.line.startswith("[C]") or self.line.startswith("[D]")
    def is_image_need(self):
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
        self.questions = []
        self.indexs = {"a":[],"b":[],"c":[]}

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
            rst.append(l.strip().decode("GBK"))
        f.close()
        return rst

    def run(self):
        self.readFiles()
        self.process_questions()
        print len(self.raw_questions_lines)
        self.indexs["a"] = self.process_indexs(self.raw_a_indexs[0])
        print "A level: %d, %d" % (len(self.raw_a_indexs), len(self.indexs["a"]))
        self.indexs["b"] = self.process_indexs(self.raw_b_indexs[0])
        print "B level: %d, %d" % (len(self.raw_b_indexs), len(self.indexs["b"]))
        self.indexs["c"] = self.process_indexs(self.raw_c_indexs[0])
        print "C level: %d, %d" % (len(self.raw_c_indexs), len(self.indexs["c"]))

        self.write_to_file("db.json", json.dumps({"questions":self.questions,"indexs":self.indexs}))

    def process_indexs(self, idxs):
        rst = []
        # sp = unicode('，' , errors='ignore')
        sp = ' '
        for _ in idxs.split(sp):
            # print _.strip()[0:6]
            rst.append(_.strip()[0:6])
        return rst

    def process_questions(self):
        l = line_processer()
        rst = None
        for _ in self.raw_questions_lines:
            rst = l.process(_)
            if rst != None:
                self.questions.append(rst)
        self.questions.append(l.get_last())
        # print len(self.questions)
        # print self.questions[496]['answers'][2]

    def write_to_file(self, path, content):
        f = open(path, 'w')
        f.write(content)
        f.close()
def main():
    b = builder()
    b.run()

if __name__=='__main__':
    main()