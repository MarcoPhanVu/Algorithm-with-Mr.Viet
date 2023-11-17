empty_set = set()
sub_list1 = [1, 2, 3]
sub_list2 = [4, 4, 9, 8, 2, 3]
sub_list3 = [7, 7, 5, 5, 6, 6]

empty_set.update(sub_list1)
empty_set.update(sub_list3)
empty_set.update(sub_list2)

array_set = set()

array_set.extend(7)
array_set.update(7)
array_set.update(5)
array_set.update(3)


print(empty_set)
print(array_set)
