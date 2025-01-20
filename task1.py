def addition(array: list) -> list:
    for index_num in range(len(array) - 1, -1, -1):
        if array[index_num] == 9:
            array[index_num] = 0
        else:
            array[index_num] += 1
            break

    if array[0] == 0:
        return [1] + array
    return array

digits = [9, 9, 9]
print(addition(digits))