def depth(listik_in):
    if not listik_in:
        return 0

    max_depth = 1
    for el in listik_in:

        if type(el) is list:
            current_depth = depth(el) + 1

            if current_depth > max_depth:
                max_depth = current_depth

    return max_depth

listik = [1, 2, [1, [1, 2, [1, [1, 2], [1, 2, [1, 2]]], 2], 2]]
print(depth(listik))  #


# [1, 2, [1, [1, 2, [1, [1, 2], [1, 2, [1, 2]]],2], 2]]
#
#     [1, [1, 2, [1, [1, 2], [1, 2, [1, 2]]],2], 2]
#
#         [1, 2, [1, [1, 2], [1, 2, [1, 2]]],2]
#
#                 [1, [1, 2], [1, 2, [1, 2]]]
#
#                         [[1, 2], [1, 2, [1, 2]]
#                                   [1, 2]



