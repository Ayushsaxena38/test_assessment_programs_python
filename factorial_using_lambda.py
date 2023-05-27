factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)

# Example usage
number = 5
result = factorial(number)
print(result)