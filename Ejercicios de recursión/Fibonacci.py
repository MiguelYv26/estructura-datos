def fibonacci(n):
    if n == 0: 
        return 0
    elif n == 1:  
        return 1
    else: 
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def fibonacci_series(n):
    return [fibonacci(i) for i in range(n)]

print(fibonacci_series(7)) 
