with open("file.txt", "r", encoding="UTF-8") as file:
    bg = {}
    data = file.read()
    words_count = data.split()
    for i in words_count:
        if i in bg:
            bg[i] += 1
        else:
            bg[i] = 1

    print(len(words_count))
    print("Самое часто-встречающееся слово: " + str(max(bg)))
    print("Которое встречается в тексте " + str(max(bg.values())) + " раз")
