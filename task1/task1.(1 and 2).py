def random_str_gen():
    all_char = {' ', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
                '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=',
                '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[',
                '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                'z', '{', '|', '}', '~'}

    string_length = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    random_0_to_9 =  int(list(string_length)[0])
    random_length = 0
    for _ in range(random_0_to_9):
        random_length += random_0_to_9

    random_result = ''

    for _ in range(random_length):
        random_char = all_char.pop()
        random_result += random_char
        all_char.add(all_char.pop())

    yield random_result

random_string = (next(random_str_gen()))
print(random_string)


def write_to_file(random_string):
    with open('random string file.txt','a') as file:
        file.write(random_string + " ")

write_to_file(random_string)


