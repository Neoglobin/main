'''
Напишите функцию, которая будет принимать на вход список чисел и будет возвращать
кортеж из чисел, которые делятся на n-число без остатка.

1) Пусть на вход функции будет передан список [1,2,3,4,5,6,7,8,9]. Тогда функция    2) Пусть на вход функции будет передан список [5,10,15,20,25]. Тогда функция
должна вернуть кортеж (3,6,9).                                                         должна вернуть кортеж (15, 20, 25).

3) Пусть на вход функции будет передан пустой список []. Тогда функция должна вернуть
пустой кортеж.
'''

def cort(a):
    b = []
    for i in a:
        if i % 3 == 0 or i % 5 == 0:
            b += [i]
    b = b.index(15, 0)
    result = tuple(b)
    return result

print(cort([5,10,15,20,25]))
