marks_1 = [2, 3, 4, 5, 3, 4, 5, 2, 2, 5, 3, 4, 3, 5, 4]
marks_2 = [4, 2, 3, 5, 3, 5, 4, 2, 2, 5, 4, 3, 5, 3, 4]
marks_3 = [5, 4, 3, 3, 4, 3, 3, 5, 5, 3, 3, 3, 3, 4, 4]
def update_marks (marks):
    return [4 if mark == 3 else mark for mark in marks if mark != 2]

updated_marks_1 = update_marks(marks_1)
updated_marks_2 = update_marks(marks_2)
updated_marks_3 = update_marks(marks_3)

print("Обновленный список оценок 1:", updated_marks_1)
print("Обновленный список оценок 2:", updated_marks_2)
print("Обновленный список оценок 3:", updated_marks_3)