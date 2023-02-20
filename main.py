import keyboard
import time
from kant_morris_pratt import *
from naive import *
from boyer_moor import *
from rabin_karp import *
from make_a_line import *


def choosing():
    print('Нажмите на клавишу:\n"1" - наивный алгоритм\n"2" - алгоритм Рабина-Карпа\n'
          '"3" - алгоритм Бойера-Мура\n"4" - алгоритм Кнута-Морриса-Пратта\n"5" - выход')
    flag = False
    while not flag:
        if keyboard.is_pressed("1"):
            flag = True
            time.sleep(0.25)
            return 1
        elif keyboard.is_pressed("2"):
            flag = True
            time.sleep(0.25)
            return 2
        elif keyboard.is_pressed("3"):
            flag = True
            time.sleep(0.25)
            return 3
        elif keyboard.is_pressed("4"):
            flag = True
            time.sleep(0.25)
            return 4
        elif keyboard.is_pressed("5"):
            time.sleep(0.25)
            print('\nДо свидания')
            exit()


def start():
    line_for_research = zapoln()
    dictionary = dict()
    black_list = []
    alphabet = {str(x): x for x in range(0, 10)}
    choose = choosing()
    for j in range(len(line_for_research)):
        if (j != len(line_for_research) - 1) and (line_for_research[j] != '0'):
            new_line = line_for_research[j:j+2]
            if new_line not in black_list:
                if choose == 1:
                    new_count = naive(new_line, line_for_research)
                elif choose == 2:
                    new_count = rabin_karp(new_line, line_for_research, alphabet)
                elif choose == 3:
                    new_count = boyer_moor(new_line, line_for_research)
                else:
                    new_count = kmp_search(new_line, line_for_research)
                dictionary[new_line] = new_count
                black_list.append(new_line)
    print()
    return {k: v for k, v in dictionary.items() if v == max(dictionary.values())}


while __name__ == '__main__':
    print('Ответ:', start(), '\n')
