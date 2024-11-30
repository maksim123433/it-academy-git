def city_country(func, *args):
    if func == fill:
       return fill(*args)
    elif func == output:
        output(*args)

def fill(number_of_countries):
    country_city_dict = {}
    for _ in range(number_of_countries):
        items = input('Введите страну и ее города: ').split()
        country_city_dict[items[0]] = items[1:]
    return country_city_dict

def output(search, country_city_dict):
    for _ in range(search):
        city = input('Введите город для поиска: ')
        found = False
        for country, cities in country_city_dict.items():
            if city in cities:
                print(f'Город {city} расположен в стране {country}')
                found = True
        if not found:
            print('Страна не найдена')

number_of_countries = int(input('Введите количество стран - '))
country_city_dict_rez = city_country(fill, number_of_countries)


search = int(input('Введите количество городов для поиска - '))
city_country(output, search, country_city_dict_rez)
