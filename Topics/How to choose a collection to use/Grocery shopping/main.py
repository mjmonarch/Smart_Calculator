import collections

shopping_list = input().split()

counter = collections.Counter(shopping_list)
for key, value in counter.items():
    print(value, key)
