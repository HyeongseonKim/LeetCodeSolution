#_5.5.3_Ordered_Dict.py

quotes = {
    'Moe': 'A wise guy, huh?',
    'Larry': 'Ow!',
    'Curly': 'Nyuk nyuk!'
}

for stooge in quotes:
    print(stooge)

from collections import OrderedDict
# List(Tuple)
quotes = OrderedDict([
    ('Moe', 'A wise guy, huh?'),
    ('Larry', 'Ow!'),
    ('Curly', 'Nyuk nyuk')
]
)

init_quotes = OrderedDict({
    'War': 'Dangerous thing',
    'Dream': 'Come true',
    'Future': 'Look for'
})

for stooge in quotes:
    print(stooge)

for comp in init_quotes:
    print(comp)
