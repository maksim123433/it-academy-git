def FizzBuzz(start, ends):
    for num in range(start, ends + 1):
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 5 == 0 and num % 3 != 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)

FizzBuzz(1, 100)
