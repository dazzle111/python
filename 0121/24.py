#!/usr/bin/python
#coding = utf-8

import string

def main():
    str = raw_input('input a string:')
    digit = 0
    space = 0
    word = 0
    other = 0
    for s in str:
        if s.isalpha():
            word += 1
        elif s.isspace():
            space += 1
        elif s.isdigit():
            digit += 1
        else:
            other += 1

    print 'digit:',digit
    print 'space:',space
    print 'word:',word
    print 'other:',other

if __name__ == '__main__':
    main()
