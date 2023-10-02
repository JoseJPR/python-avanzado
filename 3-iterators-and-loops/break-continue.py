numbers = [1,2,3,4,5]

for number in numbers:
    if number == 3:
        break
    print(number)

print('-------------')

for number in numbers:
    if number == 3:
        continue
    print(number)