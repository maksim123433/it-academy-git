import time
def dec_time_info(func, seconds = True):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        result_time = end - start
        if seconds:
            return f"Время выполнения в секундах = {result_time}\nАргументы функции: {args}, {kwargs}"
        else:
            return f"Время выполнения в минутах = {result_time / 60}\nАргументы функции: {args}, {kwargs}"
    return wrapper


def factorial(number):
    result = 1
    time.sleep(2.1)
    for num in range(1, number + 1):
        result *= num
    return result

factor_number = 9
print(dec_time_info(factorial)(factor_number))