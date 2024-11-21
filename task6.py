def zeros(list_example):
    zero_index = 0
    for i in range(len(list_example)):
        if list_example[i] != 0:
            list_example[zero_index], list_example[i] = list_example[i], list_example[zero_index]
            zero_index += 1
list_example = [1,2, 0,0, 2, 8, 1, 10, 0, 1, 0, 0]
zeros(list_example)
print(list_example)