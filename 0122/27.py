import re

phone = "2004-959-559 # this is Phone number"
num = re.sub(r'#.*$',"",phone)
print "Phone num:",num

num = re.sub(r'\D',"",phone)
print "Phone num:",num
