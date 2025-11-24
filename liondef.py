import docx
import matplotlib.pyplot as plt
import pandas as pd


doc = docx.Document('lion.docx') #считываем docx

def preobr(doc1) :
    s1 = ''
    for i in doc1.paragraphs:
        s1 += i.text #загоняем текст в s
    s1 = s1.lower() #ставим нижний регистр
    punc = '/?!.,"«»[](){}-–:;—_123456=7890\°*' #множество символов, подлежащих удалению
    for i in range(0, len(punc)) :
        if punc[i] in s1 : 
            s1 = s1.replace(punc[i], ' ') #удаление лишних символов
    return s1

def tipwrds(s1) :
    a = s1.split() #массив обособленных слов с удаленными пробелами
    d1 = {}
    for i in a :
        if i in d1.keys() :
            d1[i][0] += 1
        else :
            d1[i] = [1, 1 / len(a) * 100]
        d1[i][1] = d1[i][0] / len(a) * 100    #создали словарь d, где ключ - слово, значение - лист, состоящий из кол-ва таких слов в тексте и его встречаемости в процентах соответственно
    return d1

def tiplttrs (s1) :
    s1.replace(' ', '')
    d1 = {}
    alf = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' #создали строку, содержащую только буквы русского алфавита
    for i in s1 :
        if i in alf : #если символ строки является русской буквой
            if i in d1.keys() :
                d1[i][0] += 1
                d1[i][1] = d1[i][0] / len(s1) * 100
            else :
                d1[i] = [1, 1 / len(s1) * 100] #то же самое, что и со словами
    return d1

def tablewrds() :
    table = pd.DataFrame(d)
    print(table) #выводим таблицу со статистикой по словам

def pltlttrs() :
    k = d2.keys()
    v = d2.values()
    plt.plot(k, v)
    plt.xlabel("Буква")
    plt.ylabel("Сколько раз встретилась")
    plt.title("Гистограмма для букв")
    plt.show() #вывод статистики букв в заданных параметрах



s = preobr(doc)
d = tipwrds(s)
d2 = tiplttrs(s)
tablewrds()
pltlttrs()