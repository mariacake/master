varsta_copil_mic = 18
varsta_copil_mare = 17

#print(varsta_copil_mic + varsta_copil_mare)
#print('copil mic', varsta_copil_mic)
#print("varsta copil mic = ", varsta_copil_mic)

nr_1 = varsta_copil_mic
nr_2 = varsta_copil_mare
nr_3 = 258
nr_4 = nr_1**3

print("rezultatul la toata treaba asta este ", nr_4 - nr_3)

nr_5 = nr_4 % nr_3

#daca rezultatul impartirii la 2 cu %, atunci numarul este par

print("nr_5", nr_5)
nr_6 = nr_4 % 2 == 1

#din moment ce expresia asta e falsa, restul e 1, nr e impar
print("nr_6", nr_6)

print("nr_6", id(nr_6))

a = 45

a > 2
a = 45 + a
print(a, type(a))
a = False

print(a, type(a))

#null din other languages - none

a = None
print(a)

a = "b"
print(ord(a), type(a))

a = "7"
print(ord(a), type (a))

print(chr(98))

maria = "Maria spune'Buna ziua'"
print(maria)

#ab = "Maria spune \"Buna ziua?\"""
print(a)

mes = "Mihai \\\'Maria "
print("Maria\Vlad")
print("maria \\\'maria\\\' \\\v\\\t maria")

print("Maria vrea \nsa mearga la \nmunte")

print(r"maria \\\'maria\\\' \\\v\\\t maria")

my_name = "maria"
my_age = 27

#msg = str(my_age) + str(my_name)
#print(msg)

#mess = 'my name is %s, my age is %s' % (my_name, my_age)
#print(mess)

msg = 'my name is {ala}, my age is {ana}'.format(
    ala = my_name,
    ana = my_age)
print(msg)

msg = f'my name is {my_name}, my age is {my_age}'
print(msg)

a = 3
b = "mari"
print(a == b)

a = 'aa'
b = 'aaa'
print(a == b, a is b)
print(a is b) #a==b nu este a is b

a = [1, 2, 3]
b = [1, 2]
c = a
print(a is c)
print(id(a), id(b), id(c))

#a is b =

#a = 'Abc'
#b = 'abc'
#print(a == b)