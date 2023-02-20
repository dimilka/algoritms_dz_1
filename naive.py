
'''Наивный алгоритм'''

def naive(search_line, line):
    repeat_count = 0
    len_search_line = len(search_line)
    for i in range(len(line) - len_search_line):
        if i != len(line) - len_search_line:
            if search_line == line[i:i+len_search_line]:
                repeat_count += 1
    return repeat_count