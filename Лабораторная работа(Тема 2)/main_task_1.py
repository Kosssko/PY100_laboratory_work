list_ = [8, 9, -5, -3, 1, -10, 8, -10, -5, 0, 5, -4, 0, 10, -8, 1, 6, -6, 6, -9]

unique_numbers = set(list_) # далее unique_numbers будет обозначаться как un
sum_of_un = sum(unique_numbers)
number_of_un = len(unique_numbers)
print(sum_of_un)
print(number_of_un)
print(round(sum_of_un / number_of_un, 5))