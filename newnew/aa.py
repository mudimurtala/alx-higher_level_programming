#!/usr/bin/python3
my_set = set([1, 2, 3, 4])
my_set.add(5)
my_set.remove(3)
result = 8 in my_set
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
intersection_set = my_set.intersection(other_set)





print(intersection_set)
print(union_set)
print(other_set)
print(result)
print(my_set)