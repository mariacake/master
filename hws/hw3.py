# 1


def hw_f1(*args, **kwargs):
    sum_num = 0
    for integer in args:
        if type(integer) is int:
            sum_num += integer
    return sum_num


hw = hw_f1(1, 10, 100, 'm', [5, 50, 500], param_1='abc')
print(hw)


# 2


def hw_f2(n: int) -> tuple:

    if n == 0:
        return 0, 0, 0

    sum_total, even_sum, odd_sum = hw_f2(n-1)
    sum_total += n

    if n % 2 == 0:
        even_sum += n

    else:
        odd_sum += n

    return sum_total, even_sum, odd_sum


total_g, even_g, odd_g = hw_f2(28)

print(total_g)
print(even_g)
print(odd_g)


# 3


def hw_f3():
    user_input = input('val:')
    try:
        return int(user_input)

    except ValueError:
        return 0


hw_v = hw_f3()
print(hw_v)


# 4?


def hw_f4(*args, **kwargs):
    sum_num = 0

    for int_number in args:
        if type(int_number) == int:
            sum_num += int_number
        elif type(int_number) == list:
            for number_in_list in int_number:
                if type(number_in_list) == int:
                    sum_num += number_in_list
        elif type(int_number) == str:
            try:
                int_number = int(int_number)
                sum_num += int_number
            except ValueError:
                pass
        elif type(int_number) == dict:
            for value in int_number.values():
                if type(value) == int:
                    sum_num += value
    for int_value in kwargs.values():
        if type(int_value) == int:
            sum_num += int_value
        elif type(int_value) == list:
            for value_in_list in int_value:
                if type(value_in_list) == int:
                    sum_num += value_in_list
        elif type(int_value) == str:
            try:
                int_value = int(int_value)
                sum_num += int_value
            except ValueError:
                pass
        elif type(int_value) == dict:
            for value in int_value.values():
                if type(value) == int:
                    sum_num += value

    return sum_num


hw = hw_f4(1, 2, 3, '4', [1, 2, 3], param1=[1, 2])
print(hw)
