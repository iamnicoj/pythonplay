# string formating
float1 = 654324.46345
print("{:5.2f}".format(float1))

# string interpolation
float2 = 654324.46345
print("%5.2f" % float2)

evenBetter = "than the real thing"
print(f"Even better {evenBetter}")

str = "Some Python work to Python more to Python rocks"

print(f"count python = {str.count('Python')}")
print(str.find("work"))

