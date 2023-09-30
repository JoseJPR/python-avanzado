def calcule_perimeter(**kwargs):
    print(kwargs)
    params = kwargs.items()
    print(params)
    for key, value in params:
        print('key', key)
        print('value', value)
    print(kwargs["firstName"])
    print(kwargs["lastName"])

calcule_perimeter(firstName = 'John', lastName = 'Doe')