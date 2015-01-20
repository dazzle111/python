#coding = utf-8
#!/usr/bin/python

x =int(raw_input('input x:'))
y = int(raw_input('input y:'))

operator = raw_input('input operator:')
result = {
    "+":x+y,
    "-":x-y,
    "*":x*y,
    "/":x/y
}

print result.get(operator)
