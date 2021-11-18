from collections import OrderedDict

d = OrderedDict()

d['a'] = 'a'
d['b'] = 'b'
d['c'] = 'c'
d['d'] = 'd'
d['e'] = 'e'

d.move_to_end(key='c', last=True)

print(d)

