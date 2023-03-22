#operatori, variabile si tipuri de date

print(not(5>3 and 4<6))

mariage = '27'
city = 'cluj'
print(f'my age is {mariage} and i live in {city}')
#f citeste restul variabilelor si cu {} luam valori din afara sirului
print('my age is ' + mariage + ' and i live in ' + city)

msg = 'my name is %s, i live in %s' % (mariage, city)
print(msg)

#escape cu format
mesaj = 'my age is  {1} and i live in  {0}'.format(mariage, city)
print(mesaj)
#in acolade putem pune numarul param incepand cu 0, pentru stabilirea ordinii

mesaj = 'my age is  {age} and i live in  {unde}'.format(age = mariage, unde = city)
print(mesaj)
#deci putem atribui si nume parametrilor si sa ii chemam in acolade

mesaj = f'my age is  {mariage} and i live in {city}'
print(mesaj)

#folosim format in loc de f string cand numele sunt f lungi la variabile

# LISTELE

list1 = [2, 3, 5, 8, 35, 2889, 38, 553, 'a', 'bb', 'maria']
sliced = list1[2:5:2]
print(sliced)

slicedsimple = list1[:-5]
print(slicedsimple)  # se iau elementele fara ultimele 5, pentru ca merge - 5, - 4, - 3, - 3 ..

print(list1.count(2))

list1.insert(1, 'hhh')
print(list1)
#putem face slice si pe string, pentru ca se comporta ca o lista de caractere

mystring = 'maria e frumoasa'
list2 = mystring[1:]
print(list2)

#metodele de append, insert etc modificam lista initiala, deci ar trebui facuta o copie si copia modificata

cos = "mere, pere, struguri"
lala3 = cos.split(", ")
print(lala3)

lala2 = " ala ".join(lala3)
print(lala2)

#de la list la string si invers

# TUPLURI

months_tuple = ('ian', 'feb', 'mar', 'apr', 'mai', 'iun', 'iul', 'aug', 'sep')

# DICTIONARE

mariadict = {'maria': 27, 'alex': 24, 'iulia': 21, 3: [1, 2, 3], (1, 2, 3): 'abc', 27: {'mari': 'vlad'}, 'vlad': 247}
    # ('vlad', 2) == (8, 10)}

print(mariadict['vlad'])

print(mariadict[(1, 2, 3)])

print('alex')




