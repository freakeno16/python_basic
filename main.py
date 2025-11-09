# Распечатать все слова, в которых есть бука "о" и выбросить из текста, текст в конце рапечатать.

text = 'Sed vitae justo malesuada, commodo libero eu, bibendum mauris.'
new_text = text.split()

words = []
for word in new_text:
    if 'o' in word:
        print(word)
    else:
        words.append(word)
print(f"Words without 'o': {' '.join(words)}")




