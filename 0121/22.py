#!/usr/bin/python
#coding = utf-8
#ËØÊı
def main():
    n = int(raw_input('enter a number:'))
    print n,'='
    while(n != 1):
        for i in range(2,n+1):
            if(n % i) == 0:
                n /= i
                if(n == 1):
                    print '%d'%(i)
                else:
                    print '%d *'%(i)
                break

if __name__ == "__main__":
    main()
