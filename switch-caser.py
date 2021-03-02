# Python does not support Switch case statement by default
# you can simulate the behavior a s Switch statement encapsulating
# it in a custom function

def switcher(ID):
    switcherMap = {
        "1093" : "Nico",
        "1033" : "Jimenez",
        "1043" : "Martinez"
    }
    '''is this a comment is this a comment'''
    return switcherMap.get(ID, "Nada")

ID = "100"
while ID != "99":
  ID = input("Enter you ID: ")
  print(switcher(ID))


