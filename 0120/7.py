#!/usr/bin/python
#coding=utf-8
#问题，若字典里面的age字段是int型的话~~就不能用
import os

def find_data(data,dic):
    if(dic.has_key(data)):
        return dic.get(data)
    else:
        for key,value in dic.items():
            for dat in value.values():
                if data == dat:
                     return dic.get(key)
    return 'nothing'

dic = {'john':{'name':'john','age':'28','sex':'male'},'ligang':{'name':'ligang','age':'20','sex':'female'}}
data = raw_input('input your data:')
result = find_data(data,dic)
print result

