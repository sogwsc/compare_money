# -*-coding: utf-8 -*-

from itertools import *

def test_method(listA, listB):
    select = product(range(2), repeat=len(listA))
    data = [list(compress(listA, e)) for e in select]
    for e in data:
        if sum(e) in listB:
            for i in e:
                indexA = listA.index(i)
                listA.pop(indexA)
                print '已做账的银行记录为:%s' % i
            indexB = listB.index(sum(e))
            listB.pop(indexB)
            print '已做账的余额记录为:%s' % sum(e)
            print '------------------'
            test_method(listA, listB)

    return listA, listB


