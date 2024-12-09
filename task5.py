def closing():
    count = 0
    def counter():
        nonlocal count
        count += 1
        return count
    return counter

first_check = closing()
first_check()
first_check()
print(f'Счетчик после первого присвоения - {first_check()}')

second_check = closing()
second_check()
print(f'Счетчик после второго присвоения - {second_check()}')
