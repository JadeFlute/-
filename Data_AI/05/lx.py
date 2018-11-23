import re

s = '112122@.qqcom'
p = re.compile(r'^[0-9a-zA-Z_.-]+@[0-9a-zA-Z_-]+\.[a-zA-Z_-]+$')

r3 = p.findall(s)
print(r3)

















