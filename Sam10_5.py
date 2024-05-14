class NegativeNumberError(Exception):
    """Исключение, возникающее при попытке использования отрицательного числа."""
    def __init__(self, number):
        self.number = number
        super().__init__(f"Отрицательное число {number} не допускается.")

def divide_positive_numbers(a, b):
    if b <= 0:
        raise NegativeNumberError(b)
    return a / b

try:
    result = divide_positive_numbers(10, -2)
    print(f"Результат деления: {result}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

def get_positive_number():
    number = float(input("Введите положительное число: "))
    if number <= 0:
        raise NegativeNumberError(number)
    return number

try:
    user_number = get_positive_number()
    print(f"Вы ввели положительное число: {user_number}")
except NegativeNumberError as e:
    print(f"Ошибка: {e}")

divide_positive_numbers(10, -10)
get_positive_number()