one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]

a_min = min(one)
b_min = min(two)
c_min = min(three)

p_min = (a_min + b_min + c_min) / 2

s_min = (p_min * (p_min - a_min) * (p_min - b_min) * (p_min - c_min)) ** 0.5

print('Треугольник из минимальных значений списков: ' + str(s_min))

a_max = max(one)
b_max = max(two)
c_max = max(three)

p_max = (a_max + b_max + c_max) / 2

sq = (p_max * (p_max - a_max) * (p_max - b_max) * (p_max - c_max)) ** 0.5
s_max = round(sq, 1)

print('Треугольник из максимальных значений списков: ' + str(s_max))