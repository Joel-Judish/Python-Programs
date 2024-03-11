def fibonacci(limit):
    """Generate Fibonacci numbers up to the given limit."""
    n1, n2 = 0, 1
    while n1 <= limit:
        yield n1
        n1, n2 = n2, n1 + n2

# Only compute Fibonacci numbers up to 100
fibs = fibonacci(100)

# Lazily consume Fibonacci numbers as needed
for fib in fibs:
    print(fib)
