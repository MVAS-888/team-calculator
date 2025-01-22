import math
from math import log10, log, e
from basic_operations import add, divide, modulo, multiply, subtract
from complex_operations import ln, factorial
from sin_cos_operations import sin_number, cos_number
from new_operations_for_calculator import pow_n, square_root


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


menu_operations_mapping = {
    "1": [add, 2],
    "2": [subtract, 2],
    "3": [multiply, 2],
    "4": [divide, 2],
    "5": [modulo, 2],
    "6": [log, 2, ["Введіть число під логарифмом:", "Введіть базу логарифму:"]],
    "7": [ln, 1],
    "8": [log10, 1],
    "9": [factorial, 1],
    "10": [pow_n, 2, ["Введіть число:", "Введіть ступінь числа"]],
    "11": [square_root, 1],
    "12": [sin_number, 1],
    "13": [cos_number, 1],
}


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

        config = menu_operations_mapping[choice]

        func, expected_numbers = config[0], config[1]
        custom_input_message = config[2] if len(config) == 3 else None

        numbers = get_user_input(expected_numbers, custom_input_message)
        result = func(*numbers)

        print("Результат:", result)
