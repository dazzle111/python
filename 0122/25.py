#coding = utf-8
#!/usr/bin/python
#s=a+aa+aaa+aaaa+aa...a

def main():
    basic = int(raw_input('input a basic number:'))
    n = int(raw_input('input a number:'))
    b = basic
    sum = 0
    num = 0
    for i in range(0,n):
        if i == n-1:
            num = (10*num)+basic
            print num
            sum += num
            print sum
        else:
            num = (10*num)+basic
            sum = sum + num
            print num,'+'
    

if __name__ == '__main__':
    main()
