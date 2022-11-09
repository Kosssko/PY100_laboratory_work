from random import randint

start = -10
finish = 10
list_size = 15


def get_unique_list_numbers() -> list[int]:
    list_ = []
    while len(list_) != list_size:
        i = randint(start, finish)
        if i not in list_:
            list_.append(i)
    return list_


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
