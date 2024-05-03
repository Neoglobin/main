def sort(tp,val):
    try:
        first_index = tp.index(val)
    except ValueError:
        return ()

    try:
        second_index = tp.index(val, first_index + 1)
        return tp[first_index:second_index + 1]
    except ValueError:
        return tp[first_index:]

elem = 8

tp_1 = (1,2,3)
tp_2 = (1,8,3,4,8,8,9,2)
tp_3 = (1,2,8,5,1,2,9)

print(sort(tp_1,elem))
print(sort(tp_2,elem))
print(sort(tp_3,elem))
