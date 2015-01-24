import urllib2

Str = raw_input('input page :')
stri = 'http://'+Str
h = urllib2.urlopen(stri).read()
f = open('1.txt',"w")
f.write(h)
f.close()
print h
