#!/usr/bin/python3
# my_set = set([1, 2, 3, 4])
# my_set.add(5)
# my_set.remove(3)
# result = 8 in my_set
# other_set = {3, 4, 5, 6}
# union_set = my_set.union(other_set)
# intersection_set = my_set.intersection(other_set)
# difference_set = my_set.difference(other_set)
# subset_set = my_set.issubset(other_set)
# my_set_copy = my_set.copy()
# set_a = set([1, 2, 3, 4, 5])
# set_b = {3, 4, 5, 6, 7}
# symmetric_difference_set = set_a.symmetric_difference(set_b)
# difference_update_set = set_a.difference_update(set_b)
# disjoint_set = set_a.isdisjoint(set_b)
# frozen_set = frozenset({1, 2, 3, 4, 5})
# square_set = {x**2 for x in range(1, 11)}
# original_list = [1, 2, 2, 3, 4, 4, 5]
# original_list = set(original_list)
# set_c = set(['apple', 'banana', 'orange'])
# #x = int(input("Please enter an imteger: "))
# #if x < 0:
# #    x = 0
# #    print("Negative changed to zero")
# #elif x == 0:
# #    print("zero")
# #elif x == 1:
# #    print("single")
# #else:
# #    print("more")
# set_d = set(['banana', 'orange', 'kiwi'])
# common_elements = set_c.intersection(set_d)



# # print(common_elements)
# # print(set_c, end="\n")
# # print(set_d)
# # print(original_list)
# # print(original_list)
# # print(square_set)
# # print(frozen_set)
# # print(disjoint_set)
# # rint(difference_update_set)
# # print(symmetric_difference_set)
# # print(set_a, set_b)
# #print(my_set_copy)
# #print(subset_set)
# #print(difference_set)
# #print(intersection_set)
# #print(union_set)
# #print(other_set)
# #print(result)
# #print(my_set)


# #words = ['cat', 'window', 'defenestrate']
# #for yes in words:
# #    print(yes, len(yes))

# # Create a sample collection
# #users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# # Strategy:  Iterate over a copy
# #for user, status in users.copy().items():
# #    if status == 'inactive':
# #        del users[user]

# #print(users)    short Alake copy childrenchildrenchildrenchildrenchildren

# children = {'Alani': 'tall', 'Alamu': 'short', 'Alake': 'tall'}
# children = {'Alani': 'tall', 'Alamu': 'short', 'Alake': 'tall'}

# for child, height in children.copy().items():


# for child, height in children.copy().items():


# for child, height in adults.copy().items():

# for child, height in adults.copy().items():


# for child, height in adults.copy().items():

# tuple



# # Strategy:  Create a new collection



#                     adults = {'Alani': 'tall', 'Alamu': 'short', 'Alake': 'tall'}
#                     for child, height in children.copy().items():
#                     if height == 'short':
#                     del children[child]
#                     print(children)


# #active_users = {}
# #for user, status in users.items():
# #    if status == 'active':
# #         active_users[user] = status

# #print(active_users)

# #tall_children = {}
# #for child, height in children.items():
# #     if height == 'tall':
# #          tall_children[child] = height

# #print(tall_children)


# #zz = list(range(-10, -100, -30))
# #print(zz)

# #a = ['Mary', 'had', 'a', 'little', 'lamb', 2]
# #for items in range(len(a)):
# #    print(items, a[items])


# #a = range(6, 15, 3)
# #print(a)

# age = eval(input("Enter age: "))

# if age < 5:
#     print("Too young for School")

# elif age == 5:
#     print("Go to Kindergarten")
# elif (age > 5) and (age <= 17):
#     grade = age -5
#     print("Go to {} grade".format(grade))

# else:
#     print("Go to collage")


# for i in range(2, 10):
#     print("i =", i)

# for i in range(1, 21):
#     if ((i % 2) == 0):
#         print("i =", i)

# your_float = input("Enter a float: ")
# your_float = float(your_float)
# print("Round to 2 decimals : {:.2f}".format(your_float))

# money = input("How much to invest : ")
# interest_rate = input("Interest Rate : ")
# money = float(money)
# interest_rate = float(interest_rate) * .01
# for i in range(10):
#     money = money + (money * interest_rate)

# print("Investment after 10 years : {:.2f}".format(money))


# i = .111111111111111111111111111111111111111
# j = .000000000000000000000000100000000000001

# print("Answer : {:.32}".format(i + j))


# 

# tree_height = input("How tall is your Tree : ")
# tree_height = int(tree_height)
# spaces = tree_height - 1
# hashes = 1
# stump_spaces = tree_height - 1
# while tree_height != 0:
#     for i in range(spaces):
#         print(' ', end="")
#     for i in range(hashes):
#         print('#', end="")
#     print()
#     spaces -= 1
#     hashes += 2
#     tree_height -= 1


# for i in range(stump_spaces):
#      print(' ', end="")
# print("#")  

# for mur in range(1, 99):
#     print("{:02d}".format(mur), end=", ")
#     if mur == (98):
#         print(99)

# fav_food = input("What is my favourite food: ")

# if fav_food == "amala":
#     print("Yep! So amazing!")
# else:
#     print("Yuck! That's not it!")
# print("Thanks for playing!")







# def wash_car(amount_paid):
#     if (amount_paid == 12):
#         print("Wash with tri-color foam")
#         print("Rinse twice")
#         print("Dry with large blow dryer")

#     if (amount_paid == 6):
#         print("Wash with white foam")
#         print("Rinse once")
#         print("Air dry")


# def withdraw_money(current_balance, amount):
#     if (current_balance >= amount):
#         current_balance = current_balance - amount
#         return current_balance

# balance = withdraw_money(100,80)

# if (balance <= 50):
#     print("WE need to make a deposit")
# else:
#     print("Nothing to see here!")






# def favorite_city(name):
#     print("One of my favorite cities is", name)

# favorite_city("Makka, Saudi Arabia.")
# favorite_city("Madinah, Saudia.")
# favorite_city("Al-Quds, Palestine.")
# favorite_city("Hong Kong and Beijing, People's Republic of China")
          







# guests = [
#     'Maria',
#     'Gordon',
#     'Bob',
# ]

# cities = [
#     'Tokyo',
#     'Dakar',
#     'Mumbai',
#     'Buinos Aires',
# ]


# food = {
#     'appetizer' : 'humus',
#     'entree' : 'gyro wraps',
#     'dessert' : 'baklava',
# }


# # California state symbols
# # stateBird = 'California quail'
# # stateAnimal = 'Grizzly bear'
# # stateFlower = 'California poppy'
# # statefruit = 'Avocado'

# california_symbols = {
#     'bird' : 'California quial',
#     'animal' : 'Grizzly bear',
#     'flower' : 'California poppy',
#     'fruit' : 'Avocado',
# }

# print(cities[3])
# print(cities[2])
# print(california_symbols['animal'])
# print(california_symbols['bird'])
# print(california_symbols['flower'])









# # nearest stars to Earth
# star1 = 'Sol'
# star2 = 'Alpha Centauri'
# star3 = 'Barnard'
# star4 = 'Wolf 359'


# # nearest peak on each tectonic plate
# African = 'Kilimanjaro'
# Antarctic = 'Vinson'
# Australian = 'Puncak Jaya'
# Eurasian = 'Everest'
# North_America = 'Denali'
# Pacific = 'Mauna Kea'
# South_America = 'Aconcagua'

# stars = [
#     'Sol',
#     'Alpha Centauri',
#     'Barnard',
#     'Wolf 359',
# ]

# print(stars[3])

# peaks = {
#     'African' : 'Kilimanjaro',
#     'Antarctic' : 'Vinson',
#     'Australian' : 'Puncak Jaya',
#     'Eurasian' : 'Everest',
#     'North_America' : 'Denali',
#     'Pacific' : 'Mauna Kea',
#     'South_America' : 'Aconcagua',
# }

# print(peaks['Pacific'])











# spices = [
#     'salt',
#     'pepper',
#     'cumin',
#     'turmeric',
# ]
# for spice in spices:
#     print(spice)
# print("No more boring omelettes!")




# i = 5
# print("Count to 100 by fives:")
# while i <= 100:
#     print(i)
#     i += 5
# print("List complete!")









# fruits = [
#     'apples',
#     'bananas',
#     'dragon fruit',
#     'mangos',
#     'nectarines',
#     'pears',
# ]

# print("Our fruit selection:")
# for fruit in fruits:
#     print(fruit)



