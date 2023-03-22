def mariafunct(mar):
    print(mar)


def vladfunct(vla):
    vla('hello?')


vladfunct(mariafunct)

def mariafunct(mar):
    print(mar)


def altfunct():
    return mariafunct()


# print(altfunct())

variab = mariafunct

mariafunct('hello')

def newfunct(*args):
    s = 0

    for n in args:
        s += n

    return s
print(newfunct(27, 678))



def functie(param):
    print('acum printam prima functie', param)

def nouafunctie(functieparametru):
    print(functie)

nouafunctie(functie(27))

