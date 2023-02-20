
'''Алгоритм Бойера-Мура'''

def pre_search(pattern):
    black_list = set()
    skip_dict = {}
    for i in range(len(pattern) - 2, -1, -1):
        if pattern[i] not in black_list:
            skip_dict[pattern[i]] = len(pattern) - i - 1
            black_list.add(pattern[i])
    if pattern[len(pattern) - 1] not in black_list:
        skip_dict[pattern[len(pattern) - 1]] = len(pattern)
    return skip_dict



def boyer_moor(pattern, text):
    n = len(text)
    m = len(pattern)
    count = 0
    skip_dict = pre_search(pattern)
    if n >= m:
        i = m - 1
        while i < n:
            k = 0
            flag = False
            for j in range(m - 1, -1, -1):
                if text[i-k] != pattern[j]:
                    if j == m - 1:
                        off = skip_dict[text[i]] if skip_dict.get(text[i], False) else len(pattern)
                    else:
                        off = skip_dict[pattern[j]]
                    i += off
                    flag = True
                    break
                k += 1
            if not flag:
                count += 1
                i += 1
    return count