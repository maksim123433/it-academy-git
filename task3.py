def simultaneously(list1, list2):
    list_1 = [number for number in list1 if type(number) is int or type(number) is float]
    list_2 = [number for number in list2 if type(number) is int or type(number) is float]
    set_1 = set(list_1)
    set_2 = set(list_2)
    return len(set_1.intersection(set_2))

list_1_start = [1, 2, 'three', '4', 5, 6, 7, 8 , 1, 2, 2.1]
list_2_start = ['eight', 2, 5, 7, 8 ,12, 5, 8, 3.1, 2.1]

print(simultaneously(list_1_start, list_2_start))