cars = ["BMW", "Mercedes", "Toyota", "Tesla"]

print(cars)

# Stack methods
cars.append("Audi")
print(cars)

cars.insert(2, "Volvo")
print(cars)

# Stack methods
item = cars.pop()
print(cars)

cars.extend(["Renault", "Porsche"])
print(cars)

print("Count BMW")
print(cars.count("BMW"))

print(f"index Tesla = {cars.index('Tesla')}")

if "asdf" not in cars: print("asdf doesn't exist")

print("Reverse ")
cars.reverse()
print(cars)

cars.sort()
print("Sort ")
print(cars)

myTuples = ("something", "to", "say", "about", "tuple")
otherTuples = ("maybe", "about", "python")

listOfTuples = [myTuples, otherTuples]
print(listOfTuples)

listComprehension = [str for str in myTuples]
print(listComprehension)

othercomprehension = [char for char in "gimme love"]
print(othercomprehension)

##############
print('\n\nslicing problems:')
start = 2
stop = 5
a = [1,2,3,4,5,6,7,8]
print(a[start:stop])  # items start through stop-1
print(a[start:])      # items start through the rest of the array
print(a[:stop])       # items from the beginning through stop-1 
print(a[:])           # a copy of the whole array

print(a[-1])    # last item in the array
print(a[-2:])   # last two items in the array
print(a[:-2])   # everything except the last two items

print(a[::-1])    # all items in the array, reversed
print(a[1::-1])  # the first two items, reversed
print(a[:-3:-1])  # the last two items, reversed
print(a[-3::-1])  # everything except the last two items, reversed

