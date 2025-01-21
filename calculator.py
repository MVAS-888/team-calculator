import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Помилка: ділення на нуль"

def modulo(a, b):
    return a % b

# OLGA: sin(a)
def sin_number(a: float) -> float:
    return math.sin(a)


# OLGA: cos(a)
def cos_number(a: float) -> float:
    return math.sin(a)

def menu():
    print("\nМеню:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")
    print("5. Остача від ділення (%)")
    print("6. Sinus (sin)")
    print("5. Cosinus (cos)")
    print("0. Вихід")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Оберіть операцію: ")
        if choice == "0":
            print("Дякуємо за використання калькулятора!")
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
            try:
                if choice in ["6", "7"]:
                    num = float(input("Введіть число для обчислення: "))
                    if choice == "6":
                        print("Результат:", sin_number(num))
                    elif choice == "7":
                        print("Результат:", cos_number(num))
                else:
                    num1 = float(input("Введіть перше число: "))
                    num2 = float(input("Введіть друге число: "))
                    if choice == "1":
                        print("Результат:", add(num1, num2))
                    elif choice == "2":
                        print("Результат:", subtract(num1, num2))
                    elif choice == "3":
                        print("Результат:", multiply(num1, num2))
                    elif choice == "4":
                        print("Результат:", divide(num1, num2))
                    elif choice == "5":
                        print("Результат:", modulo(num1, num2))
                    elif choice == "5":
                        print("Результат:", modulo(num1, num2))
                    elif choice == "6":
                        print("Результат:", sin_number(num1))
                    elif choice == "7":
                        print("Результат:", cos_number(num1))
            except ValueError:
                print("Помилка: введіть коректне число!")
        else:
            print("Невірний вибір, спробуйте ще раз.")
