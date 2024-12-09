# многоразовое
def closing(num_closing):
    result = num_closing
    def multiplication(multiplier):
        nonlocal result
        result = result * multiplier
        return result
    return multiplication

num_in_closing = 5
first_check = closing(num_in_closing)
num_in_multiplication = 3
print(f'После запуска первой проверкаи - {first_check(num_in_multiplication)}')

num_in_closing = 4
second_check = closing(num_in_closing)
num_in_multiplication = 6
print(f'После запуска второй проверкаи - {second_check(num_in_multiplication)}')

num_in_closing = 5
third_check = closing(num_in_closing)
num_in_multiplication = 3
print(f'После запуска 3.1 проверкаи - {third_check(num_in_multiplication)}')
third_check(num_in_multiplication)
print(f'После запуска 3.3 проверкаи - {third_check(num_in_multiplication)}')
