# Regular Expressions First Examples

import re

pattern = re.compile('this')
string = 'search inside of this text please!'

print('search' in string)

a = re.search('this', string)
print(a.span())
print(a.start())
print(a.end())
print(a.group())

b = pattern.search(string)
c = pattern.findall(string)
d = pattern.fullmatch(string)
e = pattern.match(string)
print(b)
print(c)
print(d)
print(e)
