# 11 - 1      +1
# 111 - 3     +2
# 1111 - 6    +3
# 11111 - 10  +4
# 111111 - 15 +5

def kol_pare(list_one, set_our):
    for el in set_our:
        quantity = 0
        for counter in range(list_one.count(el)):
                quantity = quantity + counter
        print(f'Пар {el} в этом списке = {quantity} ')
our_list = [1,1, 2, 1,3, 1, 2,2,3 ,2, 2,7]
set_our = set(our_list)
kol_pare(our_list, set_our)