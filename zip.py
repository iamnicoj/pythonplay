names = ['peter', 'clark', 'bruce']
heroes = ['spiderman', 'superman', 'batman']
universe = ['marvel', 'dc', 'dc']

for values in zip(names, heroes, universe):
    print(values)

for name, hero, uni in zip(names, heroes, universe):
    print(f"{name} is {hero} in {uni}")



