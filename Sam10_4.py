import math
import functools
def precision_decorator(precision):
    """
    Декоратор для округления результатов выполнения функции до указанной точности.

    :param precision: Желаемая точность (количество десятичных знаков).
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Вызываем исходную функцию
            result = func(*args, **kwargs)

            # Округляем результат до указанной точности
            rounded_result = round(result, precision)

            return rounded_result

        return wrapper

    return decorator

# Пример использования декоратора для функции вычисления площади круга
@precision_decorator(precision=2)
def calculate_circle_area(radius):
    """
    Функция для вычисления площади круга по заданному радиусу.

    :param radius: Радиус круга (вещественное число).
    :return: Площадь круга (вещественное число).
    """
    try:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")
        return math.pi * (radius ** 2)
    except(ValueError) as e:
        print(f"ERROR: {e}")
@precision_decorator(precision=2)
def calculate_sphere_volume(radius):
    """
    Функция для вычисления объема шара по заданному радиусу.

    :param radius: Радиус шара (вещественное число).
    :return: Объем шара (вещественное число).
    """
    try:
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом.")

        volume = (4 / 3) * math.pi * (radius ** 3)
        return volume
    except(ValueError) as e:
        print(f"ERROR: {e}")


print(calculate_circle_area(3.5))
print(calculate_sphere_volume(4))
print(calculate_sphere_volume(-10))

