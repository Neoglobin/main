import re
import math

with open("input.txt", "r") as input_file, open("output.txt", "w") as output_file:

    numbers = input_file.read().splitlines()

    for number in numbers:
        try:
            number = int(number)
        except ValueError:
            number = float(number)

    result = math.pow(number, 2) + 10 * number - 15

    output_file.write(str(result) + "\n")

    input_file.close()
    output_file.close()