
'''Алгоритм Рабина-Карпа'''

def get_hash(line, alphabet):
    line_len = len(line) - 1
    line_hash = sum([alphabet[line[i]] * len(alphabet)
                     ** (line_len - i) for i in range(len(line))])
    return line_hash



def rabin_karp(pattern, line, alphabet):
    count = 0
    pattern_hash = get_hash(pattern, alphabet)
    for i in range(0, len(line) - len(pattern) + 1):
        check_line = line[i:i + len(pattern)]
        line_hash = get_hash(check_line, alphabet)
        if line_hash == pattern_hash:
            if pattern == check_line:
                count += 1
    return count