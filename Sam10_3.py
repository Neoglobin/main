def sum():
    try:
        val = int(input("Введите число: "))
        result = 2 + val
        print(result)

    except(ValueError):
        print(f"ERROR: Неподходящий тип данных. Ожидалось число")

sum()