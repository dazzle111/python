#coding = utf-8
#!/usr/bin/python

fo = open('1.txt','r')
while 1:
    str = fo.readline();
    if not str:
        break
    print str
