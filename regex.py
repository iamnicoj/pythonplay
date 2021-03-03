import re

message = ""

while message != "exit":
    message = input("Input string: ")
    print('\n')
    pattern = input("Input string: ")


    result = re.match(pattern, message)

    if result:
        print("Pattern matched!")
    else:
        print("Not luck try again :(")


