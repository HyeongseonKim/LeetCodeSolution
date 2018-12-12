#_5.5.5_itertools.py
# https://docs.python.org/3/library/itertools.html

import itertools
# itertools have lots of iterable function

# return generator who returns iterable one by one
for item in itertools.chain([1,2], ['a', 'b']):
    print(item)

# return generator who returns iterable infinitly
for item in itertools.cycle([1,2]):
    print(item)

# return generator who returns iterable one by one
for item in itertools.accumulate([1,2,3,4]):
    print(item)
