import math
from math import log10, log, e
from basic_operations import add, divide, modulo, multiply, subtract
from complex_operations import ln, factorial
from sin_cos_operations import sin_number, cos_number


def display_menu():
    print("\nМеню:")
    print("1. Додавання (+)")
    print("2. Віднімання (-)")
    print("3. Множення (*)")
    print("4. Ділення (/)")
    print("5. Остача від ділення (%)")
    print("6. Логарифм числа (log (base) num)")
    print("7. Натуральний логарифм (lg num)")
    print("8. Десятичний логарифм числа (log (10) num)")
    print("9. Факторіал (!num))")
    print("10. Ступінь (num^num)")
    print("11. Квадратний корень числа (sqrt(num))")
    print("12. Sin (sin)")
    print("13. Cos (sin)")
    print("0. Вихід")


def get_user_input(expected: int, input_messages: list[str] = None) -> list[int]:
    """
    Asks user to input one or more Z numbers.

    :param int expected: Amount of numbers to be inputed by user
    :param input_messages: Customize input message for each number input

    :raises IndexError: if input_message is not None and len(input_message) != expected
    
    :return tuple of numbers

    """
    if input_messages and len(input_messages) != expected:
        raise IndexError("Length of input messages should be same as expected amount")

    numbers = []
    counter = 0
    while counter < numbers:
        num: str = input(
            input_messages[counter] if input_messages else "Введіть число: "
        )
        if num.isalnum() or num[0] == "-" and num[1:].isalnum:
            numbers.append(int(num))
        else:
            print("Невалідне число. Доступні лише цілі, позитивні та від'ємні числа")
            continue
        expected -= 1


menu_operations_mapping = {}


if __name__ == "__main__":
    while True:
        display_menu()
        choice = input("Оберіть операцію: ")

        if choice == "0":
            print("Дякуємо за використання калькулятора!")
            break
        elif choice not in menu_operations_mapping:
            print("Такої опції не існує!")
            continue

        

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

        elif choice in ["6", "7", "6", "9"]:
            num1 = float(input("Введіть число"))
            if choice == "6":
                num2 = float(input("Введіть базу логарифма"))
                print("Результат:", log(num1, num2))
            elif choice == "7":
                print("Результат:", ln(num1))
            elif choice == "8":
                print("Результат:", log10(num1))
            elif choice == "9":
                print("Результат:", factorial(num1))
        elif choice in ["10"]:
            x = float(input("Въведете число x: "))
            n = float(input("Въведете степен n: "))
            if choice == "10":
                result_pow = x ** n
                print(f"{x}^{n} = {result_pow}")
        elif choice in ["11"]:
            value = float(input("Въведете число за квадратен корен: "))
            if choice == ["11"]:
                result_sqrt = math.sqrt(value)
                print(f"sqrt({value}) = {result_sqrt}")
        elif choice in ["12", "13"]:
            num = int(input("Введіть число: "))
            if choice == "12":
                print("Результат:", sin_number(num))
            elif choice == "13":
                print("Результат:", cos_number(num))
        else:
            print("Невірний вибір, спробуйте ще раз.")
