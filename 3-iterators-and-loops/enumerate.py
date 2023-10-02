names = ["john", "other", "example"]

for index, name in enumerate(names):
    print(index)
    print(name)

print("-------------")

names = ["john", "other", "example"]

for index, name in enumerate(names, start=1):
    print(index)
    print(name)