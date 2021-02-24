import math
x = 5 
n = 3

power = x ** n
print("%d to the power of %d is %d" % (x,n,power))  

power = pow(x,n)
print("%d to the power of %d is %d" % (x,n,power))  

power = math.pow(x,6.5)
print("%d to the power of %d is %5.2f" % (x,n,power))  
