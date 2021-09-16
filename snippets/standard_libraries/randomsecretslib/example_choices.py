import random

alist = [i for i in range(100)]
# select 10 random items from a list
print(random.sample(alist, k=10))

short_list = ["A", "V", "P", "U"]
print(random.choices(short_list, k=10))  # ['U', 'U', 'U', 'V', 'A', 'U', 'A', 'A', 'U', 'U']
