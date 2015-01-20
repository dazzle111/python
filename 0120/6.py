#!/usr/bin/python
#coding=utf-8
import os

def find_name(name,dic):
    for key,value in dic.items():
        if name == key:
            return 'key:',key,'value:',value
        else:
            pass
    return 'nothing'

dic = {'john':{'name':'john','age':28,'sex':'male'},'ligang':{'name':'ligang','age':20,'sex':'female'}}
flag = True
while(flag):
    name = raw_input('input your name:')
    result = find_name(name,dic)
    print result
    if result == 'nothing':
        pass
    else:
        flag = False
    
