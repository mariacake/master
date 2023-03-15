
tries = 3
while tries > 0:
    try:
        age = int(input('age: '))
        if age>=18:
            print('u are grown up')
        elif age<18:
            print('u are a child')
            break
    except ValueError:
        tries = tries - 1
        print('not a number')


