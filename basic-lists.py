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

print ([0] * 10)
print ([2,3,5,] == 8)