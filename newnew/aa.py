#!/usr/bin/python3
my_set = set([1, 2, 3, 4])
my_set.add(5)
my_set.remove(3)
result = 8 in my_set
other_set = {3, 4, 5, 6}
union_set = my_set.union(other_set)
intersection_set = my_set.intersection(other_set)
difference_set = my_set.difference(other_set)
subset_set = my_set.issubset(other_set)
my_set_copy = my_set.copy()
set_a = set([1, 2, 3, 4, 5])
set_b = {3, 4, 5, 6, 7}
symmetric_difference_set = set_a.symmetric_difference(set_b)
difference_update_set = set_a.difference_update(set_b)


print(difference_update_set)
print(symmetric_difference_set)
print(set_a, set_b)
print(my_set_copy)
print(subset_set)
print(difference_set)
print(intersection_set)
print(union_set)
print(other_set)
print(result)
print(my_set)