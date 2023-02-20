
'''Алгоритм Кнута-Морриса-Пратта'''

def pi(pattern):
    p = [0] * len(pattern)
    i = 0
    j = 1
    while j < len(pattern):
        if pattern[i] == pattern[j]:
            p[j] = i + 1
            i += 1
            j += 1
        else:
            if i == 0:
                p[j] = 0
                j += 1
            else:
                i = p[i - 1]
    return p


def kmp_search(pattern, text):
    count = 0
    n = len(text)
    i, j = 0, 0
    p = pi(pattern)
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                count += 1
                i += 1
                j = 0
        else:
            if j > 0:
                j = p[j-1]
            else:
                i += 1

    return count

