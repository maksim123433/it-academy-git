def create_dict():
    start_dictionary = {}
    count = 1
    def inner(word):
        nonlocal start_dictionary
        nonlocal count
        start_dictionary[count] = word
        count += 1
        return start_dictionary
    return inner

f_1 = create_dict()
print(f_1('hello'))
print(f_1('hello')) # f_1 возвращает {1: 'hello'}
print(f_1(100)) # f_1 возвращает {1: 'hello', 2: 100}
print(f_1([1, 2, 3])) # f_1 возвращает {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()
print(f_2('PoweR'))
