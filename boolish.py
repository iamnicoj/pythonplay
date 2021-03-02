var1 = True
print( "var1 = True")
print(bool(var1))

try:
  var2 = "true"
  print("var2 = \"true\"")
  print(bool(var2))
except ValueError:
  print("SomeError")

try:
  var22 = "false"
  print("var2 = \"false\"")
  print(bool(var22))
except ValueError:
  print("SomeError")

try:
  var22 = ""
  print(f"var2 = {var22}")
  print(bool(var22))
except ValueError:
  print("SomeError")

number = 10
print("number = 10")
print(bool(number))

number = -40
print("number = -40")
print(bool(number))

number = 0
print("number = 0")
print(bool(number))

number = 0.5
print("number = 0.5")
print(bool(number))

print("print(bool(6<3)")
print(bool(6<3))

