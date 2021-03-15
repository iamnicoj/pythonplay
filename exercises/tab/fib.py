def fib(num):
    if num == 0: return 0
    fib_cache = [0 for _ in range(num + 1)]

    fib_cache[1] = 1

    for i in range(num + 1):
        if i < 2: continue
        # IT IS KEY TO PAY STRONG ATTENTION TO THE MATH FORMULA 
        # AND KEEP IT MIND THIS IS NOT DOING DECREASING RECURSIVE
        fib_cache[i] = fib_cache[i - 1] + fib_cache[i-2] 
    
    return fib_cache[num]

print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))
print(fib(70000))

