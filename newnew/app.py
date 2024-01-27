# import testmodule
# testmodule.mult(5, 10)

# year = 2016
# event = 'Referendum'
# f'Results of the {year} {event}'
# print(f'Results of the {year} {event}')

# yes_votes = 42572654
# no_votes = 43132495
# percentage = yes_votes / (yes_votes + no_votes)
# print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

# s = 'Hello, world.'
# str(s)
# print(s)
# repr(s)
# print(repr(s))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      

# str(1 / 7)
# print(str(1/7))

# x = 10 * 3.25
# y = 200 * 200
# s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
# print(s)
# print(f'The value of x is {x}, and y is {y}...')


# m = 'mudi\n'
# mm = repr(m)
# print(mm)

# ss = str(m)
# print(ss)

# import math
# print(f'The value of pi is approximately {math.pi:.3f}.')



# table = {
#     'Sjoerd' : 4127,
#     'Jack' : 4098,
#     'Dcab' : 7678,
# }

# for person, number in table.items():
#     print(f'{person:10} ==> {number:10d}')



#     animals = 'eels'
#     print(f'My pool is full of {animals}')
#     print(f'My pool is full of {animals!r}')
#     print(f'My pool is full of {animals!a}')
#     print(f'My pool is full of {animals!s}')
#     print(f'My pool is full of {animals=}')



#     print('We are the {} who say "{}"!'.format('Knights', 'Ni'))
#     print('who is the {1} who slapped the {0}'.format('girl', 'boy'))
#     print('who is the {a} who slapped the {b}.'.format(a='tall boy', b='big girl'))


#     for m in range(0, 15):
#         print('{0:2d} {1:3d} {2:4d}'.format(m, m*m, m*m*m))




# value = input('Enter a number: ')
# print(value + ' is my favourite number!')
# print("When you multiply it by 10, this is what you get:")
# value_int = int(value)
# print(value_int * 10)


# first_name = 'malala'
# last_name = 'yousafzai'
# note = 'award: Nobel Peace Prize'
# first_name_cap = first_name.capitalize()
# last_name_cap = last_name.capitalize()
# print(first_name_cap)
# print(last_name_cap)
# award_location = note.find('award: ')
# peace_location = note.find('Peace')
# print(peace_location)
# print(award_location)
# award_text = note[7:]
# print(award_text)

# import re
# five_digit_zip = '98101'
# nine_digit_zip = '98101-0003'
# phone_number = '234-567-8901'
# five_digit_expression = r'\d{5}'
# print(re.search(five_digit_expression, five_digit_zip))
# print(re.search(five_digit_expression, nine_digit_zip))
# print(re.search(five_digit_expression, phone_number))


# miles = input('Enter a distance in miles: ')
# # Kilometers_value = miles_value * 1.609344
# miles = float(miles)
# value_entered = float(miles)
# value_entered = value_entered * 1.609344
# print(f'{miles} miles is equal to {value_entered} kilometers')







# miles = input('Enter a distance in miles: ')
# # Kilometers_value = miles_value * 1.609344
# miles_float = float(miles)
# kilometers = miles_float * 1.609344
# print('That value in kilometers is', end=' ')
# print(kilometers)




# def check_temp(temp):
#     if temp < 15:
#         print('Wear a jacket')
#     elif temp > 25 and temp <= 35:
#         print('Pack a jacket')
#     elif temp > 35:
#         print('Leave the jacket at home')

# check_temp(10)
# check_temp(30)
# check_temp(37)



# def plant_recomendation(care):
#     if care == 'low':
#         print('aloe')
#     elif care == 'medium':
#         print('pothos')
#     elif care == 'high':
#         print('orchid')

# plant_recomendation('low')
# plant_recomendation('medium')
# plant_recomendation('high')







# class Person:
#     def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
#         self.age = age
#         self.weight = weight
#         self.height = height
#         self.first_name = first_name
#         self.last_name = last_name
#         self.catch_phrase = catch_phrase

#     def walk(self):
#         print("Walking...")

#     def run(self):
#         print("Running...")

#     def sleep(self):
#         print("Sleeping...")

# user = Person(29, 60, 160, "murtala", "mudi", "You must win the competition, Mudi Murtala")

# print(user.catch_phrase)
# user.walk()
# user.sleep()

# class Shago:
#     def __init__(self, adreshi, girma, fadi, suna, lamba, kudinsa):
#         self.adreshi = adreshi
#         self.girma = girma
#         self.fadi = fadi
#         self.suna =suna
#         self.lamba = lamba
#         self.kudinsa = kudinsa

#     def itace(self):
#         print("Akwai Itace da yawa")

#     def masallaci(self):
#         print("Ee, akwai masallaci guda daya aicki")

#     def rijiya(self):
#         print("A a, babu rijiya aciki")


# nadaya = Shago("Opposite Road Safety", "Eka Goma(10)", "Gaba Ashirin(20)", "Garejin Alhaji Mudi", 171, "Miliyan Dari(100)")
# print(nadaya.girma)
# print(nadaya.kudinsa)
# print(nadaya.suna)
# print(nadaya.lamba)

# nadaya.itace()
# nadaya.masallaci()
# nadaya.rijiya()


# class Bottle:
#     def __init__(self, volume, type_):
#         self.volume = volume
#         self.type_ = type_

#     def pour(self):
#         print("Pouring...")

#     def fill(self):
#         print("Filling...")

#     def recycle(self):
#         print("Recycling...")





# flips = [
#     'heads',
#     'tails',
#     'tails',
#     'heads',
#     'tails',
# ]

# print(flips.count('heads'))
# print(flips.pop())


# class Attendee:
#     'Common base class for all attendees'

#     def __init__(self, name, tickets):
#         self.name = name
#         self.tickets = tickets

#     def displayAttendee(self):
#         print('Name : {}, Tickets: {}'.format(self.name, self.tickets))

#     def addTicket(self):
#         self.tickets += 1
#         print('{} tickets increased to {}'.format(self.name, self.tickets))


# attendee1 = Attendee('B. Giles', 2)
# attendee2 = Attendee('J. Ortega', 1)

# attendee2.addTicket()
# attendee2.addTicket()

# attendee1.displayAttendee()
# attendee2.displayAttendee()


# s = "x is"
# x = 13 % 3 * 2
# print(s, x)


# value = 1
# count = 0
# while value < 20:
#     value += 4
#     count += 1
# print("reached", value,"after",count,"iterations")



# def equal(x,y):
#     if x == y:
#         print(x + y)
#     else:
#         print(x = y)
# equal(1,2)


# myfile = open('myfile.txt', 'wt')
# print('hello', file=myfile)

# nums = [1, 2, 3, 4, 5]
# sum = 0
# for num in nums:
#     sum += num

# print(sum)


# num = input('Your number?')
# print('Your number squared is', num*num)

# the_name_of_the_class = "python 101"
# print(the_name_of_the_class)

# classname = "python 101"
# print(classname)

# def sqr(x):
#     # print("the square root of {x} is {x*x}")
#     # print(f"the square root of x is x^2")
#     print(f"the square root of {x} is {x*x}")
#     print("the square root of x is x*x")
# sqr(4)


person = {
    "name" : "Sunita",
    "phone" : "212-515-5555",
    "address" : ["123 Main St", "Sydney"]
}
address = person["address"]
city = address[1]
print(city)
print(person["address"][1])
#print(person[1])












