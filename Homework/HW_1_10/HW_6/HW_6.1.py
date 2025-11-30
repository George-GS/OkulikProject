# Распечатать все слова, в которых есть бука "о"
# и выбросить из текста, текст в конце рапечатать.

text = 'Sed vitae justo malesuada, commodo libero eu, mauris.'
print(text)

o_word = []
bad_word = []
words = text.split()
print(f'Список слов: \n{words}')

for word in words:
    if 'o' in word:
        o_word += [word]
    else:
        bad_word += [word]


finaly_text = ' '.join(bad_word)

print(f'Слова с буквой "о": {o_word}')
print(f'Текст без слов с буквой "о": {finaly_text}')

