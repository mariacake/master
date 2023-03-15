# while True:
#     try:
#         age = int(input('age: '))
#     except ValueError:
#         print('not a number')
#         continue
#
#     if age >= 18:
#         print('go in')
#     else:
#         print('u no in')



tries = 3
while tries > 0:
    try:
        age = int(input('age: '))
        if age>=18:
            print('u grown')
        elif age<18:
            print('u not')
            break
    except ValueError:
        tries = tries - 1
        print('not a number')




# print('not a number')
# age = int(input('age: '))
#     try:
#         tries = 3
#         while tries > 0:
#             tries = tries - 1
#     except ValueError:




# except ValueError:
#     while tries>0:
#         print('not a number')
#         tries = tries - 1



