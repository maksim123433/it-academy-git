def factorial(number):
    if number == 1:
       return 1
    return number * factorial(number - 1)

number_factorial = 4
print(factorial(number_factorial))
