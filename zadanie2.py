import wikipedia


def make_a_True_text(text):
    bad = '.,?/><":;][{}\|/=-`~!@#$%^&«»*()_+—'
    for i in bad:
        text = text.replace(i, '')
    j = 2
    while ' ' * j in text:
        text = text.replace(' ' * j, ' ')
    text = text.replace("'", "")
    text = text.replace('о́', 'о')
    return text.lower()


wikipedia.set_lang("ru")

wiki = wikipedia.page("Астероид")
text1 = make_a_True_text(' '.join(wiki.content.strip().split()).strip())
file = open('Астероид.txt', 'r', encoding='utf-8')
all_lines = file.readlines()
file.close()

original = make_a_True_text(' '.join(wiki.content.strip().split()).strip())
nashe = make_a_True_text(' '.join(i.replace('\n', '') for i in all_lines))




all_words = list(set((original + ' ' + nashe).split()))
d = {all_words[i]: i for i in range(len(all_words))}
original_mas = [d[i] for i in original.split()]
nashe_mas = [d[i] for i in nashe.split()]

i, j = 0, 0
count = 0
total = 0
flag = True
while j < len(nashe_mas):
    while (i < len(original_mas)) and (nashe_mas[j] == original_mas[i]):
        i += 1
        j += 1
        count += 1
        if j >= len(nashe_mas):
            flag = False
            break
    if flag:
        if count >= 3:
            total += count
            j += 1
            i = 0
            count = 0
        elif count == 0:
            if nashe_mas[j] in original_mas:
                i += 1
            else:
                j += 1
        else:
            i = 0
            count = 0

print('Процент плагиата', round(total/len(nashe_mas) * 100, 2), '%')
