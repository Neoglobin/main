with open("input.txt", "r", encoding="UTF-8") as file:
    data = file.read()
    words_count = data.split()

with open("input.txt", "r", encoding="UTF-8") as file:
    lines = file.readlines()

print("Input file contains: ")
print(str(len(data)) + " letters")
print(str(len(words_count)) + " words")
print(str(len(lines)) + " lines")
