number_list = [1, 2, 3, 4, 5]
result_map_object = list(map(lambda num: { "num": num, "other": num*2}, number_list))
print(result_map_object)

