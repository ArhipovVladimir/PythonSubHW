'''В большой текстовой строке подсчитать количество
встречаемых слов и вернуть 10 самых частых.
Не учитывать знаки препинания и регистр символов.
За основу возьмите любую статью из википедии или из
документации к языку.'''

text = 'высокоуровневый язык программирования общего назначения с динамической строгой' \
' типизацией и автоматическим управлением памятью, ориентированный на повышение' \
'  производительности разработчика, читаемости кода и его качества, а также на обеспечение' \
'  переносимости написанных на нём программ. Язык является полностью объектно-ориентированным' \
'   в том плане, что всё является объектами. Необычной особенностью языка является выделение' \
'   блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего ' \
'  на практике редко возникает необходимость обращаться к документации. Сам же язык известен ' \
'  как интерпретируемый и используется в том числе для написания скриптов. Недостатками ' \
'  языка являются зачастую более низкая скорость работы и более высокое потребление памяти написанных' \
'   на нём программ по сравнению с аналогичным кодом, написанным на компилируемых языках, таких как C или C++.'

LIMIT = 10

split_text = text.replace(',', ''). \
        replace('.', ''). \
        replace('!', ''). \
        replace('?', ''). \
        replace('"', ''). \
        lower().split()

dict_count_word = {}

# print(split_text)
for word in split_text:
    if split_text.count(word) not in dict_count_word:
        dict_count_word[split_text.count(word)] = set(word)
    dict_count_word[split_text.count(word)].add(word)

# print(max(dict_count_word.keys()))

coun = 0
for number, word in dict_count_word.items():
    print(f'колличество {number}, слова {word}')
    coun += 1
    if coun > LIMIT:
        break

