def increase(number):
    return number + 1

numbers = [1,2,3,4,5]

result_example_b = [ increase(number) for number in numbers ]
print(result_example_b)

print('----------------')

result_example_a = [ number + 1 for number in numbers ]
print(result_example_a)