num_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6, 0]
sort_list = sorted(num_list)

print(num_list)
print(sort_list)

sort_list.reverse()
print(sort_list)

print(len(sort_list))
slice_list0 = sort_list[0::2]
print(slice_list0)

slice_list1 = sort_list[1::2]
print(slice_list1)

slice_list2 = sort_list[1::3]
print(slice_list2)

slice_list2 = sort_list[6::2]
print(slice_list2)
