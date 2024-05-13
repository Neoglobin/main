def file_reading(filename, method):
    try:
        with open(filename, method) as file:
            result = file.read()
            if len(result) == 0:
                raise IOError("Файл пуст")

            print(result)

    except(IOError) as e:
        print(f"ERROR: {e}")

file_reading("empty.txt", "r")
file_reading("filled.txt", "r")
