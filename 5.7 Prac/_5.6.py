#_5.6.py
from pprint import pprint


plain = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

from collections import OrderedDict

fancy = OrderedDict(plain)

pprint(plain)
pprint(fancy)

for key, value in fancy.items() :
    print(key, ": ", value)
