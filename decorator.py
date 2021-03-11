def decorate(func):
   def wrapper(*args):
       print("Before Hello World")
       func(*args)
       print("After Hello World")
   return wrapper

def validate(func):
    def wrapper(*args):
   		print("Validating User", args[0])
   		func(*args)
    return wrapper

@decorate
@validate
def hello_world(name):
     print(f"Hello World {name}")

hello_world("Nick here")

print('is there someone out there?')