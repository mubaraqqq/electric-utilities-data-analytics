# name = 'Matt'
# first = name
# age = 1000

# print(id(age))
# age += 1
# print(id(age))

# names = []
# print (id(names))
# names.append('Fred')
# print(id(names))
# print(dir())
# #Exercises
# num = 5.1
# print(num)
# print(id(num))
# print(type(num))
# num += 20
# print(num)
# print(id(num))
# print(type(num))

# list_one = []
# print(list_one)
# print(type(list_one))
# print(id(list_one))
# list_one.append(300)
# print(list_one)
# print(type(list_one))
# print(id(list_one))

# #Numbers
# print(1.01-.99)
# print(type('num: %s' %2))
# print('num: %s' %2)
# print('4' * 2)
# print('Python ' * 3)

# import operator
# print(operator.add(2,5))
# print(operator.countOf('book', 'o'))

# print ((6.2 +7.8 + 6.5 + 7.1 +8.5)/3)
# if 297 % 3 == 0 :
#     print('297 is divisible by 3')

# def leap_year (x) :
#     if x % 4 == 0 or x % 400 == 0:
#         print(str(x) + ' is a leap year')
#     else :
#         print(str(x) + ' is not a leap year')    

# print(leap_year(1800))
# print(leap_year(1900))
# print(leap_year(1903))
# print(leap_year(2000))
# print(leap_year(2002))

#Strings
#to include backlashes in strings
# backslash = '\\'
# print(backslash)
# #formatting strings
# name = 'Matt'
# print('Hello {}'.format(name))
# print('Name: {:*^12}'.format('Ringo'))
# print('Percent {:=+10.1%}'.format(-44/100))
# print('Binary: {:b}'.format(12))

# namme = 'Mubaraq'
# age = 19
# print(namme + ' is ' + str(age))
# print('{}'.format(namme) + ' is ' + '{}'.format(age))
# paragraph = '''\"Python is a great language!",
#  said Fred. "I don't ever remember having this
#  much fun before." '''
# print(paragraph)
# print('{}'.format('\u03A9'))

# item = 'car'
# cost = 13499.99
# print('{:<}'.format(item) +'{: >20,}'.format(cost))

#dir, help and pdb
# print(dir('Mubaraq'))
# print(dir(90))


# country = 'usa'
# correct_country = country.upper()
# print(correct_country)

# filename = 'hello.py'
# print(filename.endswith('java'))
# print(filename.find('py'))
# print(filename.startswith('world'))

#Comments, Boolean and None
# names = ()
# if names :
#     print ('Class has enrollments')
# else :
#     print('The class is empty')    
# car = None
# if car :
#     print('Taxi for you!')
# else :
#     print('The taxi is not here yet') 
# age = 5
# old = age > 18       
# print (old)

#Conditionals and whitespace
# leap = 8
# print(leap % 4 == 0) 


# print(leap % 2 == 1)

# #Containers: Lists, Tuples and Sets
# print(set([1, 5, 'pool']))
# names = ['Bayo', 'George', 'Indabosky',
#          'Ayomikun', 'Ayokunmi', 'Ayomide']
# print(id(names))
# names.append('Florence')
# names.append('Nightingale')
# print(names)
# print(id(names))
# names.sort()
# print(names)
# print(names[0])
# print(names[1])

# tuple1 = ('Mubaraq', 'Mustapha', 19)
# people = []
# people.append(tuple1)
# tuple2 = ('Tumilara', 'Adesanya', 19)
# tuple3 = ('Mubashir', 'Mustapha', 15)
# tuple4 = ('Oluwadarasimi', 'Adeboyeku', 20)
# people.append(tuple2)
# people.append(tuple3)
# people.append(tuple4)
# print(people)
# people.sort()
# print(people)

# name1 = ['Mubaraq', 'Tumilara', 'Georgia',
#          'Flintstone', 'Harriet']
# common_names = ['Adam', 'Jake', 'Elizabeth',
#          'Esther', 'John', 'Jack', 'Mubaraq']
# print(set(name1) & set(common_names))

# print(help())

#Iteration
# for letter in ['c', 'a', 't'] :
#     print (letter)

# print(letter)

# names = ['Mubaraq', 'Tumilara', 'Georgia',
#           'Flintstone', 'Harriet']

# counter = 0
# for items in names :
#     for letters in items :
#         counter += 1
# name_len = len(names)
# average_length = counter / name_len
# print (average_length)

# for item in names :
#     if item == 'John' :
#         break
#     else :
#         print('Not found')

# lists = [('Mubaraq', 'Mustapha', 19),
#          ('Tumilara', 'Adesanya', None), 
#          ('Mubashir', 'Mustapha', 15), 
#          ('Oluwadarasimi', 'Adeboyeku', 20)]
# counters = 0
# none_type = 0
# for item in lists :
#     for info in item :
#         if info is None :
#             continue
#         elif isinstance(info, str) :
#             continue
#         elif isinstance(info, int) :
#             counters += info
#         else :
#             print ('No age values have been inputed')
#     for info in item :
#         if info is None :
#             none_type += 1
#         else :
#             continue
# list_length = len(lists) - none_type
# if not counters :
#     print ('Average values can\'t be calculated as a result of invalid age values')
# else :
#     average_age = counters / list_length
#     print(average_age)
# for item in lists :
#     for info in item :
#         if isinstance(info, int) and info > average_age :
#             print ('{}, {} old'.format(item[0], item[1]))
#         elif isinstance(info, int) and info < average_age :
#             print ('{}, {} young'.format(item[0], item[1]))
#         elif info is None :
#             print('Age not defined')

#Dictionaries
# data = {'Adam': 2, 'Zeek': 5, 'Fred': 3}
# print (data.keys())

# info = {'first': 'Mubaraq', 'last': 'Mustapha',
#         'age': 19}
# phone = {}
# phone['screen size'] = 10
# phone['memory'] = 8
# phone['OS'] = 'Android'
# phone['brand'] = 'Samsung'
# phone.setdefault('price', 20000)
# print(phone)

# par = '''Dictionaries provide quick lookup or insertion for a key. You can also do
# a lookup by value, but it is slow. If you find yourself doing this operation
# often, it is a code smell that you should use a different data structure.'''
# par_split = par.split()
# par_dict = {}
# counter = 0
# for item in par_split :
#     counter += 1
#     par_dict.setdefault(counter, []).append(item)
# print(par_dict)

# from collections import Counter
# print(Counter(par_split))

# dict1 = []
# dict2 = []
# dict_remove = []
# counters = 0
# for item in par_split : 
#     counters += 1
#     if len(ite)
    

#Functions
def is_odd (x) :
    if x % 2 == 0 :
        return False
    else :
        return True
print(is_odd(8))