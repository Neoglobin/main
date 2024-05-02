def renew_tp(tp1, tp2, tp3):
    list_1 = []
    list_2 = []
    list_3 = []
    for sub_tp in tp1:
        list_1 = list(tp1[0])
        if list_1[0] == 1:
            list_1.pop(0)
        else:
            return tp1

    list_2 = list(tp2[0])
    list_3 = list(tp3[0])
    result_1 = tuple(list_1)
    result_2 = tuple(list_2)
    result_3 = tuple(list_3)
    return result_1, result_2, result_3

a = ((1,2,3),1)
b = ((1,2,3,1,2,3,4,5,2,3,4,2,4,2),3)
c = ((2,4,6,6,4,2),9)

print(renew_tp(a,b,c))
