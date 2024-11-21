# list_result = []
# def list_1(list_base, number_of_letters):
#     for i in range(len(list_base) -number_of_letters ):
#         for j in range(i,len(list_base)):
#             if j != 0:
#                 list_result.append(list_base[i] + list_base[j])
#     return list_result
# list_base = ['a', 'b', 'c', 'd']
# rez = (list_1(list_base, 2))#['ab', 'ac', 'ad', 'bb', 'bc', 'bd'].
# print(' '.join(rez))

print('Пункт 1')
def punct_1(list_base,number_of_letters):

    list_result = [i + j for i in list_base if list_base.index(i) <  number_of_letters
                            for j in list_base if list_base.index(i) <= list_base.index(j) < len(list_base) and list_base.index(j) > 0]
    return list_result

list_base = ['a', 'b', 'c', 'd']
number_of_letters = 2
print((punct_1(list_base,number_of_letters)))



print('Пункт 2')
def punct_2():
    result = punct_1(list_base,number_of_letters)
    print(result[:3])

punct_2()# ['ab', 'ad', 'bc'].




print('Пункт 3')
def punct_3(num1, num2, char):
    return [str(i) + char for i in range(num1, num2 + 1)]

char = 'a'
num1 = 1
num2 = 4
print(punct_3(num1, num2, char))




print('Пункт 4')
def punct_4(listik,delete):
    listik.remove(delete)
    return listik
delete = '2a'
print(punct_4(punct_3(num1, num2, char), delete))




print('Пункт 5')
def punct_5(listik_base, insert_what, index_what):
    listik = listik_base.copy()
    listik.insert(index_what, insert_what)
    print(listik)
    print(f"Основной - {listik_base}")
insert_what = '2a'
index_what = 1
punct_5(punct_4(punct_3(num1, num2, char), delete), insert_what, index_what)