import re

pattern = re.compile(r'(\d+)@(\w+)\.\w+')

s = '12312423@qq.com'
print pattern.search(s)
