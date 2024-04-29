checks = [8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321, 3365,1478, 9865, 5555, 7777, 9998, 1111, 2222,3333, 4444, 5556, 6666,
5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365, 7502, 3016, 4928,5837, 3365, 8201, 5410, 2643, 7168, 5017, 7777, 9682, 9865, 8530, 5678,
3250, 8201, 7193, 4445, 9051, 3016, 4506, 4506, 1987,4506]

print('Количество чеков: ' + str(len(checks)))

count = {}
differences = 0
max_value = 0
id = 0
for i in checks:
    if i in count:
        count[i] += 1
    else:
        count[i] = 1

    if count[i] > 1:
        differences += 1


    max_value = max(count.values())


print('Количество гостей: ' + str(55-differences))

for j in count.keys():
    if count[j] == max_value:
        id = j

print('Работник с id - ' + str(id) + ', посетивший ресторан в количестве ' + str(max_value) + ' раз.')


