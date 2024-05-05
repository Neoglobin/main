import datetime
import os

cathegories = {
    "Продукты": {

    },
    "Развлечения": {

    },
    "Прочее": {

    }
}
def insert(ask):
    if ask in cathegories:
        cathegories[ask] = "Дата: " + str(datetime.date.today()) + "; Значение: " + input("Значение расхода: ")
        save(ask)
    elif ask == "Стоп":
        exit()
    else:
        print("Ошибка ввода")

def save(ask):
    with open("file.txt", "a", encoding="UTF-8") as file:
        file.write("\n" + "__________________________________________________________________________")
        file.write("\n" + "Новая запись: " + str(datetime.date.today()) + "; Категория - " + ask)
        file.write("\n" + cathegories[ask])
        return insert(input("Категория расходов: "))

filename = "file.txt"

if os.path.exists(filename):
    insert(input("Категория расходов: "))
else:
    print("ERROR: File does not exist")





