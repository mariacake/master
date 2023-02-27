# # a = 15
# print(a)
# #erorile sunt exceptii nameerror - faptul ca a nu e definit
# #in fisierul blabla la linia respectiva,
# # print('valid instruction')
#
# a = '12'
# b = int(a)
#
# print(a, type(a))
# # print(b, type(b))    metoda input
#
# user_input = input('insert a number:')
# user_input = int(user_input)
# print('user_input =', user_input, type(user_input))          #practic noi anticipam ce poate sa puna utilizatorul, deci tratam exceptia
#
# #ne folosim try except
#
# user_input = input('insert a number: ')
#
# try:
#     user_input = int(user_input)
#     print(undef)
# except Exception as e:
#     print(e, type(e))
#     print('u stupid try a number')
#
# try:
#     user_input = int(user_input)
#     print(undef)
# except ValueError as e:
#     print(e, type(e))
#     print('u stupid try a number')
# except NameError as e:
#     print('u stupid we dont have undef')
# else if elif merg pe valori booleene
#

# import sys
#
# user_age = input("age pls: ")
# try:
#     user_age = int(user_age)
#
# except ValueError:
#     print('u stupid thats not a number')
#
# else:
#     if user_age >= 18:
#         print('you grown')
#         sys.exit(0)
#     else:
#         print('uu u try')
#         #fie punem si asta intr un try except, fie folosim try else
#
# finally:
#     print('haha u done')

# user_age = int(input('age please: '))
#
# if user_age >= 18:
#     print('u old haha')
# elif user_age >= 30 and user_age <50:
#     print('u very old haha')
# else:
#     print('u drool')
# #
# while type(user_age) == int:
#     print('boo')
# my_list = [67, 89, 34, 67, 35]
#
# print(list(enumerate(my_list)))
#
# my_set = set(my_list)
# for item in my_set:
#     print(item)
#
# #pentru a vedea la al catelea pas suntem
#
# for item in my_list:
#     print(f'item with value = {item} is on index = {my_list.index(item)}')
#
# #returneaza mereu indexul primei intalniri cu valoarea
#
# for element in enumerate(my_list):                 #enumerate ne da mereu secvente de tupluri
#     print(element, type(element))
#
# for item in my_list:
#     print(f'item with value = {item[2]} is on index = {element[1]}')

# my_tup = (56, -2, 14)
# print(my_tup, type(my_tup))
# a, b, c =my_tup
#
# print(a)                   #valabil la tuplu, liste
#
# for index, number in enumerate(my_tup):
#     print(f'item with value = {number} is on index = {index}')

# numbers = [12, 56, -2, 14]
# index = 0                               #index mai mic decat lungimea listei, afiseaza..
#
# while index < len(numbers):
#     print('boohooo')
#     index = index + 1
#
# is_valid = False
#
# while not is_valid:
#     age = int(input('age'))
#
#     try:
#         age = int(age)
#     except ValueError:
#         print('not a number')
#     else:
#         is_valid = True
#
#         if age >= 18:
#             print('of age!!')
#         else:
#             print('not of age!!')
# break                                    #opreste executia, transfera controlul in afara loop

for number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    if number % 2 == 0:
        print(f'is even = {number}')
        break
    else:
        print(f'is odd = {number}')


#break, continue, pass
for number in [1, 2, 3, 4]:
    pass                               #placeholder pana la finalizarea instructiunilor primite

