def fibonacci(x):
    if x == 0 or x == 1:
        return 1
    return fibonacci(x - 1) + fibonacci(x - 2)
    
