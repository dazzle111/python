#coding = utf-8
#!/usr/bin/python
#根据收入判断利润，思想是从高部分往下算

mon = [1000000,600000,400000,200000,100000,0]
rate = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
num = int(raw_input('input your salary:'))
for i in range(0,6):
    if num > mon[i]:
        r += (num-mon[i])*rate[i]
        num = mon[i]
print r
