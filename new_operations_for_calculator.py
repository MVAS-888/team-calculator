import math

x = float(input("Въведете число x: "))
n = float(input("Въведете степен n: "))


result_pow = x ** n
print(f"{x}^{n} = {result_pow}")


value = float(input("Въведете число за квадратен корен: "))


result_sqrt = math.sqrt(value)
print(f"sqrt({value}) = {result_sqrt}")