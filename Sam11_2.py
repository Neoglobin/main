def writing(func):
    def wrapper(*args, **kwargs):
        try:
            with open("fib.txt", "w", encoding="UTF-8") as file:
                for num in func(*args, **kwargs):
                    file.write(str(num) + "\n")

        except Exception as e:
            print(f"ERROR: {e}")

    return wrapper

@writing
def fib(n):
    a, b = 1, 1  # Начальные значения для чисел Фибоначчи
    count = 0  # Счетчик количества сгенерированных чисел

    while count < n:
        yield a  # Возвращаем текущее число Фибоначчи
        a, b = b, a + b  # Обновляем значения для следующего числа Фибоначчи
        count += 1


fib(200)
