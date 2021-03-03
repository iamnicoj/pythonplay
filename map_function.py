def power_of(x, n):
    return x ** n

numbers = [2, 3, 4]

value = input("Enter value: ")

import functools
result = map(functools.partial( power_of, int(value)), numbers)

print(list(result))

[power_of(x, 2) for x in [1, 2, 3]]