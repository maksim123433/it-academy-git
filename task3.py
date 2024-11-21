
base_list = ['a', 'b', 'c']
print(f'Начало с - {base_list}')

print('Пункт 1\n')
def punctt_1(list_base):
    return tuple(list_base)

print( f'{punctt_1(base_list)} -  {type(punctt_1(base_list))}')


print('Пункт 2\n')
def punctt_2(tuple_start):
    return list(tuple_start)

print( f'{punctt_2(punctt_1(base_list))} -  {type(punctt_2(punctt_1(base_list)))}')


print('Пункт 3\n')
def punctt_3(assignment):
    assignment[assignment.index('a')] = 'a'
    assignment[assignment.index('b')] = '2'
    assignment[assignment.index('c')] = 'python'
    return tuple(assignment)

print( f'{(punctt_3(list(punctt_1(base_list))))} ')


print('Пункт 4\n')
def punctt_4(element_tuple):
    if element_tuple == 0:
        return
    punctt_4(element_tuple - 1)
    print(element_tuple, end = ' ')

your_tuple = (4, )
print(f'Размер кортежа перед началом - {len(your_tuple)}, с цифрой начала - {your_tuple[0]}')
punctt_4(your_tuple[0])

