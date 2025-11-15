import docx
import matplotlib.pyplot as plt
import pandas as pd


doc = docx.Document('lion.docx') #считываем docx
s = ''
for i in doc.paragraphs:
    s += i.text #загоняем текст в s
s = s.lower() #ставим нижний регистр
punc = '/?!.,"«»[](){}-–:;—_123456=7890\°*' #множество символов, подлежащих удалению
for i in range(0, len(punc)) :
    if punc[i] in s : 
        s = s.replace(punc[i], ' ') #удаление лишних символов
    
a = s.split() #массив обособленных слов с удаленными пробелами
d = {}
for i in a :
    if i in d.keys() :
        d[i][0] += 1
    else :
        d[i] = [1, 1 / len(a) * 100]
    d[i][1] = d[i][0] / len(a) * 100    #создали словарь d, где ключ - слово, значение - лист, состоящий из кол-ва таких слов в тексте и его встречаемости в процентах соответственно

d1 = {}
s.replace(' ', '')
alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #создали строку, содержащую только буквы русского алфавита
for i in s :
    if i in alf : #если символ строки является русской буквой
        if i in d1.keys() :
            d1[i][0] += 1
            d1[i][1] = d1[i][0] / len(s) * 100
        else :
            d1[i] = [1, 1 / len(s) * 100] #то же самое, что и со словами

table = pd.DataFrame(d)
print(table) #выводим таблицу со статистикой по словам

k = d1.keys()
v = d1.values()
plt.plot(k, v)
plt.xlabel("Буква")
plt.ylabel("Сколько раз встретилась")
plt.title("Гистограмма для букв")
plt.show() #вывод статистики букв в заданных параметрах





