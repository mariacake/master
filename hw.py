num_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6, 0]
sort_list = sorted(num_list)

print(num_list)
print(sort_list)

sort_list.reverse()
print(sort_list)

print(len(sort_list))
even_num = sort_list[0::2]
print(even_num)

odd_num = sort_list[1::2]
print(odd_num)

div_3 = sort_list[1::3]
print(div_3)