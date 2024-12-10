def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
 
    product = 1
    for i in range(2, n + 1):
        product *= i
    return product
 
 
def fib(n):
    if n<3:
        return 1
    return fib(n-2)+fib(n-1)


for n in range(1, 6): # probando
    print(n, factorial_function(n))

for n in range(1, 10): # probando
    print(n, "->", fib(n))
