def set_task(list_baza):
    list_result = []
    for element in list_baza:
        if element not in list_result and list_baza.count(element) == 1:
            list_result.append(element)
    return list_result
list_for_task = [1, 2,'a', 4, 'p', 1, 'a', 4]
print(f'Элементы списка - {list_for_task} которые встречаются один раз - {set_task(list_for_task)}')