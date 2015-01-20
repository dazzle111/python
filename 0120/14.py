#!/usr/bin/python
import re

line ='Cats are smarter than dogs'

matchObj = re.sub(r'\s+','-',line)
print matchObj;
result = re.split(r'-+',line)
print result
