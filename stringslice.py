mystr = "this is a very consice phrase."
extra = "this"

print("sliceObj = slice(5)")
sliceObj = slice(5)
print(mystr[sliceObj])


print("sliceObj = slice(5, 12)")
sliceObj = slice(5, 12)
print(mystr[sliceObj])


print("sliceObj = slice(5, 25, 3)")
sliceObj = slice(5, 25, 3)
print(mystr[sliceObj])

print('advanced slicing')
print(mystr.find(extra))
sliceOjb = slice(len(extra), len(mystr))
print(mystr[sliceOjb])
