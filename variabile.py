varsta_copil_mic = 18
varsta_copil_mare = 17

print(varsta_copil_mic + varsta_copil_mare)
print('copil mic', varsta_copil_mic)
print("varsta copil mic = ", varsta_copil_mic)

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