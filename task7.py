def Evklid(first_number, second_number):
    while first_number != 0 and second_number != 0:
        if first_number > second_number:
            first_number = first_number % second_number
        else:
            second_number = second_number % first_number
    return first_number + second_number

print(f'НОД - {Evklid(30, 18)}')