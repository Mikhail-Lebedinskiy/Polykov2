def calculate_factorial(n):
  if n == 0: # выход из рекурсии
    return 1
  return n * calculate_factorial(n - 1)


print(calculate_factorial(5))
