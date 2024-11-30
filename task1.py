def Dict_comprehensions(*args, **kwargs):
    dict_base = {key :key ** 3 for key in range(1, 21)}
    return dict_base

print(Dict_comprehensions())