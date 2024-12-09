def limiter(func, limitation):
    number_of_calls = 0
    def wrapper(*args, **kwargs):
        nonlocal number_of_calls
        if number_of_calls < limitation:
            number_of_calls += 1
            return func(number_of_calls)
        else:
            return f'Вы превысили ограничение по вызовам {limitation}, вы вызвали функцию уже {number_of_calls} раз'
    return wrapper

def function(number_of_calls):
    return f'Функция отработала уже {number_of_calls} раз'

permitted_quantity = 3
decorator1 = limiter(function, permitted_quantity)
print(decorator1())
print(decorator1())
print(decorator1())

print()

permitted_quantity = 2
decorator2 = limiter(function, permitted_quantity)
print(decorator2())
print(decorator2())
print(decorator2())
print(decorator2())
