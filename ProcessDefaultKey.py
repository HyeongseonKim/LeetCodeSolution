# 5.5 Python Standard Library
'''setdefault: for using dictionary,
if key is not in dic, key will be included'''

periodic_table = {'Hydrogen': 1, 'Helium': 2}
print(periodic_table)

carbon = periodic_table.setdefault('Carbon', 12)
print(carbon)
print(periodic_table)

#if key is in dic, no adding and return original value
helium = periodic_table.setdefault('Helium', 947)
print(helium)
print(periodic_table)


'''defaultdict: for using dictionary and func from collections'''
from collections import defaultdict

# defaultdict(func, just name not ())
periodic_table = defaultdict(int)
periodic_table['Hydrogen'] = 1
print(periodic_table['Hydrogen'])
print(periodic_table['Lead'])

def no_idea():
    return 'Huh'

bestiary = defaultdict(no_idea)
bestiary['A'] = 'Abominable Snowman'
bestiary['B'] = 'Basilisk'

print(bestiary['A'])
print(bestiary['B'])
print(bestiary['C'])

bestiary = defaultdict(lambda: 'Huh?')
print(bestiary['E'])
