# -*-coding: utf-8 -*-
from itertools import *
from test2 import *
from read_txt import *

list_a = read_txt('C:\Users\Administrator\Desktop\\1.txt')
list_a = map(eval, list_a)  #银行账单
list_b = read_txt('C:\Users\Administrator\Desktop\\2.txt')
list_b = map(eval, list_b)  #做账清单

for i in list_a:
    if i in list_b:
        print '已做账的银行记录为:%f' %i
        print '已做账的余额记录为:%f' %i
        print '------------------'
        index_a = list_a.index(i)
        index_b = list_b.index(i)
        list_a.pop(index_a)
        list_b.pop(index_b)


listA, listB = test_method(list_a, list_b)
print '未做账的银行记录为:%s' % listA
print '未做账的余额记录为:%s' % listB







