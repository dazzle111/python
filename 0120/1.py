#coding=utf-8
#!/usr/bin/python

def printinfo(arg1,*vartuple):
    print "输出："
    print arg1
    for var in vartuple:
        print var
    return ;

printinfo(10);
printinfo(10,20,304,0)
