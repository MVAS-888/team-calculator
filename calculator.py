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

def menu():
    print("\nМеню:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")
    print("5. Остача від ділення (%)")
    print("0. Вихід")

if __name__ == "__main__":
    while True:
        menu()
        choice = input("Оберіть операцію: ")
        if choice == "0":
            print("Дякуємо за використання калькулятора!")
            break
        elif choice in ["1", "2", "3", "4", "5"]:
            try:
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
            except ValueError:
                print("Помилка: введіть коректне число!")
        else:
            print("Невірний вибір, спробуйте ще раз.")