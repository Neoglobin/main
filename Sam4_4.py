
def ag(*args):
        summa = sum(args)
        avg = summa / len(args)
        return avg

if __name__ == '__main__':
    print(ag(23,45,23,54,33,44))