arr = [10.2, 14.8, 19.3, 22.7, 12.5, 33.1, 38.9, 21.6, 26.4, 17.1, 30.2, 35.7, 16.9, 27.8, 24.5, 16.3, 18.7, 31.9, 12.9, 37.4]

arr.sort(reverse=True)
print('3 Лучших результата: ' + str(arr[0]) + ' ' + str(arr[1]) + ' ' + str(arr[2]))

arr.sort()
print('3 Худших результата: ' + str(arr[0]) + ' ' + str(arr[1]) + ' ' + str(arr[2]))

result = {}

for i in arr:
    if i >= 10:
        result[i] = i

print(result.values())















