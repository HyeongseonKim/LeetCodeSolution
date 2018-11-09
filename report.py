def get_description():   #  docstring right under here
    'Return random weather, just like the pros'
    from random import choice
    possibilities = ['rain', 'snow', 'sleet', 'fog', 'sun', 'who knows']
    return choice(possibilities)
