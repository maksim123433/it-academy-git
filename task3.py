def dec_for_type_check(func):
    def wrapper(*args, **kwargs):
        flag = True
        for el in args:
            if type(el) not in normal_type:
                flag = False
                break
        if flag:
            func(*args, **kwargs)
            return 'Normal type'
        else:
            raise TypeError("Вы передали не те типы данных")
    return wrapper

normal_type = (int, float, str)

def check(*args, **kwargs):
    return 0

decorator = dec_for_type_check(check)
first_attempt = decorator(1, 'mwedkmew', 1.2)
print(first_attempt)

second_attempt = decorator(1, [2, 2], 'wx', 1.1)
print(second_attempt)
