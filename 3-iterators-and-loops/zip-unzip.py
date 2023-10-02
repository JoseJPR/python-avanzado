numbers = [1,2,3,4,5]
names = ["john", "other", "example"]

zipped = list(zip(numbers, names))
print(zipped)

numbers_unzip, names_unzip = zip(*zipped)
print(numbers_unzip)
print(names_unzip)

print ("--------------")

for number, name in zip(numbers, names):
    print('number -> ', number)
    print('name -> ', name)