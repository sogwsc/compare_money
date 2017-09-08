# -*-coding: utf-8 -*-

from itertools import *

def test_method(num, listA, listB):
    print num
    new_list_a = list(permutations(listA, num))
    for e in new_list_a:
        if sum(e) in listB and set(listA) > set(e):
            for i in e:
                indexA = listA.index(i)
                listA.pop(indexA)
                print '已做账的银行记录为:%s' % i
            indexB = listB.index(sum(e))
            listB.pop(indexB)
            print '已做账的余额记录为:%s' % sum(e)
            print '------------------'

    if num < len(listA):
        test_method(num + 1, listA, listB)

    return listA, listB
