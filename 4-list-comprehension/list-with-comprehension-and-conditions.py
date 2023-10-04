def is_par(number):
    return number % 2 == 0

result_example_a = [ number + 1 for number in [1,2,3,4,5] if number > 1 ]
print(result_example_a)

print('----------------')

result_example_b = [ number + 1 for number in [1,2,3,4,5] if is_par(number) ]
print(result_example_b)

print('----------------')

result_example_c = [ number + 1 if is_par(number) else 0 for number in [1,2,3,4,5] ]
print(result_example_c)