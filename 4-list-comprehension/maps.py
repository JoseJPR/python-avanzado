def increase(number):
    return number + 1

numbers = [1,2,3,4,5]

result = map(increase, numbers)
print(list(result))