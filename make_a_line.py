
'''Создание строки простых чисел'''

def prost(x):
    return x > 1 and all(x % w != 0 for w in range(2, int(x**0.5) + 1))


def zapoln():
    now = 2
    A = []
    while True:
        if len(A) == 500:
            break
        if prost(now):
            A.append(now)
        now += 1
    stroka = ''
    for i in A:
        stroka += str(i)
    return stroka