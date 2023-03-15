#pct 1

def hw_f1(*args, **kwargs):
    sum_num = 0
    for integer in args:
        if type(integer) is int:
            sum_num += integer
    return sum_num

hw = hw_f1(3, 4, 345, 'm', [1, 2, 3], param1 = 'abc')
print(hw)

#pct 2

def hw_f2(n: int) ->tuple:
    if n == 0:
        return 0, 0, 0

    sumatotala, even, odd = hw_f2(n-1)

    sumatotala += n

    if n % 2 == 0:
        even += n

    else:
        odd += n

    return sumatotala, even, odd

sumtotal, evend, oddd = hw_f2(28)

print(sumtotal)


#pct 3

def hw_f3():
    user_input = input('val:')
    try:
        return int(user_input)

    except ValueError:
        return 0

print(hw_f3)

#tema 1



