# -*-coding: utf-8 -*-

def read_txt(path):
    with open(path, 'r') as f1:
        l1 = f1.read().replace('\n', ' ')
    l2 = l1.split()
    return l2

