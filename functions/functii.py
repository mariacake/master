# def maria():
#     print('hello function')
#     print(2+5)
#
# maria()
# def get_number():
#     number = int(input('nbs='))
#     return number
#
#
# def maria_func():
#     while True:
#         try:
#             # a = int(input('a='))
#             get_number()
#             # break
#         except ValueError:
#             print('error')

def f(param_1='abd'):
    print(param_1)

f()
f(param_1='fed')        #mod recomandat de trimis parametri, pentru ca unele au param required/pozitionali, unii cheie valoare
f()                      #daca dam nume la parametri, atunci e ok fara sa le dam si sa apelam fct f(), daca nu dam
                       #de la inceput nume, atunci treb specificati cand o apelam
                       #cei fara nume la inceput ceilalti la final

def f(a, b):
    print(a)
    print(b)
f(10, -5)

#variable length argument - parametru special care nu este folosit daca nu este declarat
#definit cu steluta *args

def f(*mine):
    print(mine)              #args la finalul param pozitionali, este un tuplu f(a, b, c, *args, f='uu')

f(5, 6, 2, 9, 10, 33)




