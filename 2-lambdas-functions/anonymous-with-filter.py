is_even = lambda num: num % 2 == 0
print(is_even(2))
print(is_even(3))

number_list = [1, 2, 3, 4, 5]
result_equal = list(filter(lambda num: num == 2, number_list))
print(result_equal)

result_filter = list(filter(lambda num: num % 2 == 0, number_list))
print(result_filter)
