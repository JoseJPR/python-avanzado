numbers = [1,2,2,3,4,4,5,6]

set_pair = { number + 1 for number in numbers if number % 2 == 0 }
print(set_pair)

set_dictionary = { number: str(number) for number in numbers if number % 2 == 0  }
print(set_dictionary)

vocals = 'aeiou'
set_dictionary_vocal = { vocal.lower(): vocal.upper() for vocal in vocals }
print(set_dictionary_vocal)