# import random
# import time
#
# # # if __name__ == '__main__':
# # #     numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
# # #     print(random.choice(numbers))
# # #
# # #     time.sleep(5)
# # #     print('the time')
# #
# # # from random import choice
# #
# # if __name__ = '__main__':
# #     max_tries = 3
# #     current_try = 1
# #     while current_try <= max_tries:
# #         user_age = input('age: ')
# #
# #         try:
# #             user_age = int(user_age)
# #         except ValueError:
# #             print('not a number')
# #             current_try += 1
# #             continue
# #
# #         if user_age <= 18:
# #             print('grown')
# #         else:
# #             print('child')
# #
# #         break
# #     else:
# #         print('invalid')
#
# # def forloop():
# #     max_tries = 3
# #     current_try = 1
# #     while current_try <= max_tries:
# #         user_age = input('age: ')
# #
# #         try:
# #             user_age = int(user_age)
# #         except ValueError:
# #             print('not a number')
# #             current_try += 1
# #             continue
# #
# #         if user_age <= 18:
# #             print('child')
# #
# #
# #         break
# #     else:
# #         print('invalid')
# #
# # def for_loop():
# #     max_tries = 3
# #     for  in range(max_tries):
# #         user_age = input('age: ')
# #
# #
# #
# #
# # if __name__ == '__main__':
# #     forloop()
#
# from time import monotonic_ns
#
#
# # def iterate_while(numbers):
# #     start_time = monotonic_ns()
# #     print('iterate w while loop')
# #     index = 0
# #     while index < len(numbers):
# #         # print(numbers[index])
# #         index += 1
# #     end_time = monotonic_ns()
# #     execution = end_time - start_time
# #     print(f'execution time: {execution}(ns)')
# #
# #
# # def iterate_for(numbers):
# #     start_time = monotonic_ns()
# #
# #     print('iterate w for loop')
# #     time.sleep(1)
# #     for number in numbers:
# #         # print(number)
# #         pass
# #     end_time = monotonic_ns()
# #     execution = end_time - start_time
# #     print(f'execution time: {execution}(ns)')
#
# # if __name__ == '__name__':
# #     numero = list(range(100))
# #     print(iterate_while(numero))
# #     print(iterate_for(numero))
#
# #mai eficient de folosit for atunci cand facem loops, pentru ca la rezultate f mari e mai rapid
#
# def execution_time(function_to_decorate):
#     def wrapper(*args):
#         start_time = monotonic_ns()
#
#         result = function_to_decorate(*args)
#
#         end_time = monotonic_ns()
#         execution = end_time - start_time
#         execution_ns = execution / 10000000
#         print(f'execution: {execution_ns}(ns)')
#         return result
#
#     return wrapper
#
#
#
# def iterate_while(numbers):
#     print('iterate with while')
#     index = 0
#     time.sleep(1)
#     while index < len(numbers):
#         index += 1
#
#
# def iterate_for(numbers):
#     print('iterate with for')
#     for number in numbers:
#         pass
#
# def s(a, b):
#     return a+b
#
#
# if __name__ == '__main__':
#     numbers = list(range(10000000))
#     print(iterate_while(numbers))
#     print(iterate_for(numbers))
#
#     decorated_iterate_while = execution_time(iterate_while)
#     decorated_iterate_while(numbers)
#     decorated_iterate_for = execution_time(iterate_for)
#     decorated_iterate_for(numbers)
#     decorated_s = execution_time(s)
#     suma = decorated_s(1, 7)                #lui decorated s i am dat un singur parametru, desi s are 2
#     print('suma', suma)
#
# #decorator = fct care primeste o functie pe care urmeaza sa o decoreze ca parametru
#
#


def dec(f):
    def wrapper(*args, **kwargs):
        print(f'before {f.__name__} call')
        result = f(*args, **kwargs)
        print(f'before {f.__name__} call')
        return result
    return wrapper


def f1():
    """
    Asta e functia ce o cream ca sa vedem documentatia.
    Aici as fi scris ce urmeaza sa faca functia.
    :param p1 No idea what is does!
    This is my fuckin function!
    """
    print('-- inside f1')


def f2(p1):
    print('-- inside f2', p1)
    """
    Asta e functia ce o cream ca sa vedem documentatia.
    Aici as fi scris ce urmeaza sa faca functia.
    :param p1 No idea what is does!
    This is my fuckin function!
    """


def f3(p1, p2, kw1=None):
    print('-- inside f3', p1, p2, kw1)


if __name__ == '__main__':
    print('f1 name', f2.__name__)
    print('f1 doc', f2.__doc__)


if __name__ == '__main__':
    decorated_f1 = dec(f1)
    decorated_f1()
    #
    # print('\n')
    #
    # decorated_f2 = dec(f2)
    # decorated_f2(10)
    #
    # print('\n')
    # decorated_f3 = dec(f3)
    # decorated_f3(12, 15, kw1='abc')

#functii deja decorate

from functools import wraps

def dec(f):
    @wraps(f)
    def f1(p):
        """
        functie decorata cu @
        :param p:
        """
        print('--inside new one', p)

f1(5)
print(f1, f1.__name__)
print(f1, f1.__doc__)               # nu avem documentatie pentru ca f1(5) returneaza wrapperul pt ca e dec.



