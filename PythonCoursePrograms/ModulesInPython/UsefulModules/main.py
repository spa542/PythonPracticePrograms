# Useful Modules 

# Specialized data types that are used from imported modules

from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
print(Counter(li))
print(Counter(sentence))

dictionary = defaultdict(lambda: 5, {'a': 1, 'b': 2})
print('Does exist')
print(dictionary['a'])
print('Does not exist')
print(dictionary['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['a'] = 2
d2['b'] = 2

print(d2 == d)

# More useful modules

import datetime

print(datetime.time(5,45,2))
print(datetime.date.today())

from array import array

arr = array('i', [1,2,3])
print(arr[0])
