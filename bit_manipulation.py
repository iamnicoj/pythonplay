def setbit(num, i):
    return num | (1 << i)

def getbit(num,i):
    return (num & (1 << i)) != 0

def clearbit(num, i):
    mask = ~(1 << i) 
    return num & mask

def clearMStoI(num, i):
    mask = (1 << i) - 1
    return num & mask

def clearIto0(num, i):
    mask = (-1 << i)
    return num & mask

def printbinary(num):
    print("{0:b}".format(num))

def updatebit(num, bit, i):
    value = 1 if bit == True else 0
    mask =  ~(1 << i)
    return num & mask | value << i


printbinary(7)
printbinary(13)
printbinary(15)

print(clearbit(15, 2))
print(clearbit(15, 0))

print(clearMStoI(15, 2))
print(clearMStoI(13, 2))

print(clearIto0(15, 2))
print(clearIto0(13, 2))
    
print(updatebit(13, 1, 1))
print(updatebit(15, 0, 1))
# print(getbit(4,2))
# print(getbit(8,2))
# print(getbit(8,3))
# print(setbit(0, 3))


# To int
print(int('0101', 2))
print(int('1010101010101', 2))

# To Hex
print("0x%x" % int('1010', 2))
print ("0x%x" % int('0010101110101100111010101101010111110101010101', 2))

# To Char
print(chr(int('1010000' , 2)))
print(chr(int('0110110' , 2)))
print(chr(int('1010101' , 2)))
print(chr(int('01110101' , 2)))
print(int('01110101' , 2))
print(ord('u'))

print(1 << 0)
print(1 << 1)
print(1 << 2)
print(1 << 3)
print(1 << 4)
print(1 << 5)
print(1 << 6)
print(1 << 7)
print(1 << 31) #Max 32bit Int

print('print binary')
print("{0:b}".format(37))

