import time
def fib_decore(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()

        execution_time = end_time - start_time
        print(f"Время выполнения: {execution_time:.6f} секунды")
        return result
    return wrapper

@fib_decore
def fibonacci():
    fib1 = fib2 = 1

    for i in range(2, 200):
        result = 0
        fib1, fib2 = fib2, fib1 + fib2
        result = fib2
    print(f"Результат равен: {result}")

if __name__ == '__main__':
    fibonacci()