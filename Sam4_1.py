from datetime import datetime # Эта строка импортирует модуль datetime из стандартной библиотеки Python. Это позволит использовать функции и классы модуля datetime в программе.
from math import sqrt # Эта строка импортирует функцию sqrt из модуля math. Функция sqrt вычисляет квадратный корень числа.

def main(**kwargs):
    '''
    def main() - Функция для вычисления квадратного корня суммы квадратов двух элементов в списке.

    :param kwargs: Аргументы принимают форму словаря kwargs.
    :return: Возвращает переменную result.
    '''
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)


if __name__ == '__main__': # Эта конструкция проверяет, является ли текущий модуль основным. Если да, то выполняются следующие строки.
    start_time = datetime.now() # Эта строка создает переменную start_time и присваивает ей значение, которое возвращает функция datetime.now(). Функция datetime.now() возвращает текущую дату и время.
    main (                          #Эта строка вызывает функцию main с аргументами в виде пар ключ-значение.
        one = [10, 3],
        two = [5, 4],
        three = [15, 13],
        four = [93, 53],
        five = [133, 15]
    )

    time_costs = datetime.now() - start_time # Эта строка вычисляет разницу между текущим временем и временем начала программы.
    print(f"Время выполнения программы - {time_costs}") # Эта строка выводит на экран сообщение о времени выполнения программы.


