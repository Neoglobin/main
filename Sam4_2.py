import random

def dice(*args):
    for val in args:
        print(val)

    if val == 5 or val == 6:
        print('Вы победили')
    elif val == 3 or val == 4:
        dice(random.randint(1, 6))
    else:
        print('Вы проиграли')

if __name__ == '__main__':
    dice(random.randint(1, 6))
