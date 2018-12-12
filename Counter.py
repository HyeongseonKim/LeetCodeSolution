#5.5.2 Counter

from collections import defaultdict
food_counter = defaultdict(int)
for food in ['spam', 'spam', 'eggs', 'spam']:
    food_counter[food] += 1

for food, count in food_counter.items():
    print(food, count)

from collections import Counter
#{Counter make dic from list, key: list itmes, value: count
#Counter have most_common() func: sorting downward by value
breakfast = ['spam', 'eggs', 'eggs', 'labstar']
lunch = ['eggs', 'eggs', 'bacon']
breakfast_counter = Counter(breakfast)
lunch_counter = Counter(lunch)

print(breakfast_counter)
print(breakfast_counter.most_common())
print(breakfast_counter.most_common(1))
print(breakfast.count('spam'))

# Counter Object's component can be merged by '+'
print(breakfast_counter + lunch_counter)
# Counter Object's component can be removed by '-'
print(breakfast_counter - lunch_counter)
# Counter Objects can be intersected by '&'
print(breakfast_counter & lunch_counter)
# Counter Objects can be unioned by '&'
print(breakfast_counter | lunch_counter)
