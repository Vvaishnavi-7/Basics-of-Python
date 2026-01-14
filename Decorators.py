import time
from functools import wraps

def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.6f} seconds")
        return res
    return wrapper

# Recursive helper function (not decorated)
def _fib_helper(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return _fib_helper(n-1) + _fib_helper(n-2)

# Top-level function decorated
@log_execution_time
def fibonacci(n):
    return _fib_helper(n)

# Test
fib = 20
result = fibonacci(fib)
print(f"Fibonacci({fib}) =", result)
