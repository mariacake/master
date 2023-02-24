#list = []
#list2 = list()

#de preferat nu varianta asta

lista = ['maria', 'alexandra', 'iulia ']
print(id(lista))

print(lista[-3])

print(len(lista))

list = [23, 45, 24, 67, 25, 69, 76, 32, 76]
a_slice = list[::]

print(a_slice)

my_list = 'maria e frumoasa'
print(my_list[3::])

#my_list_to_string = list[my_list]
#print(my_list_to_string, type(my_list_to_string))
list.append(3456)
print(list)

x = "maria vlad florin"
m = x.split(" ")
print(m)

#y = "maria are multe mere si multi struguri"
#z = y.join()

#tupluri

my_tuplu = (1,5,6,3, 'a', 'm')
#daca avem nevoie sa definim un tuplu cu mai multe obiecte
#se pun cu virgula
print(my_tuplu, type(my_tuplu))
print(my_tuplu[-3])
print(my_tuplu[::4])     #asta e slice din 4 in 4

#mine = (1, 2, 3)
#print(mine)
#minelist = list(mine)
#print(minelist)

marialist = [1, 2, 3]
mariatuple = ('a', marialist, 'b')  #putem modifica pentru ca tuplul nu l mai modificam
#modificam lista si tuplul citeste lista asa cum este in momentul respectiv

print(mariatuple)
marialist.append(18)
print(mariatuple)