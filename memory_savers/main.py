# memory savers
# functia filter

tuplu = (1, 2, 3)
lista = [1, 2, 3]           #rulam doar pe lista, dar se poate aplica pe orice str de date care poate fi iterata
sets = {1, 2, 3}
rang = range(100)

# functia filter filtreaza date

# my_range = list(range(10))
# filtered = []
# for number in my_range:
#     if number % 5 == 0:
#         filtered.append(number)
# print(filtered)

from random import shuffle

def filter_number(element):
    print('element', element)

my_range = list(range(10))
shuffle(my_range)
my_range = list(filter(filter_number, my_range))
print('my range', my_range)
