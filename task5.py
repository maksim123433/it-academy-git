def schoolchildren_and_languages(quantity):
    dict_with_schoolchildren = {}
    count = 1
    for schoolchildren in range(quantity):
        number_of_languages = int(input('Сколько языков знает школьник - '))
        list_of_languages = []
        for language in range(number_of_languages):
            language1 = input('Введите язык, который знает школьник - ')
            list_of_languages.append(language1)
        dict_with_schoolchildren[count] = list_of_languages
        count += 1
    return dict_with_schoolchildren

def search_common(dictionary, number):
    common_languages = set(dictionary[1])
    for man_index in range(2, number + 1):
        common_languages.intersection_update(dictionary[man_index])
    return list(common_languages)


def search_symmetric_difference(dictionary, number, common):
    dif_languages = set(dictionary[1])
    for man_index in range(2, number + 1):
        dif_languages = dif_languages.symmetric_difference(dictionary[man_index])
    unique_languages = dif_languages - set(common)

    return list(unique_languages)


number_of_schoolchildren = int(input('Введите количество школьников - '))
dict_schoolchildren_for_search = schoolchildren_and_languages(number_of_schoolchildren) #весь словарь
print(dict_schoolchildren_for_search)

common_lang = search_common(dict_schoolchildren_for_search, number_of_schoolchildren)
len_common_lang = len(search_common(dict_schoolchildren_for_search, number_of_schoolchildren))

print(f'Количестов языков, которыке занют все школьники - {len_common_lang}')
if len_common_lang != 0 :
    print(search_common(dict_schoolchildren_for_search, number_of_schoolchildren))

len_individual_lang = len(search_symmetric_difference(dict_schoolchildren_for_search, number_of_schoolchildren,common_lang ))

print(f'Количество индивидульных языков- {len_individual_lang}')
if len_individual_lang != 0:
    print(search_symmetric_difference(dict_schoolchildren_for_search, number_of_schoolchildren, common_lang))

