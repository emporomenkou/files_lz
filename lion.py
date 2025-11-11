import docx
import matplotlib as plt

f = open('lion.txt', 'rt', encoding='UTF-8')
input = f.read()

doc = docx.Document('lion.docx')
s = ''
for i in doc.paragraphs:
    s += i.text
s = s.lower()
punc = '/?!.,"«»[](){}-–:;—_1234567890xiv'
for i in range(0, len(punc)) :
    if punc[i] in s : 
        s = s.replace(punc[i], ' ')
    
a = s.split()
d = {}
for i in a :
    if i in d.keys() :
        d[i][0] += 1
        d[i][1] = 
    else :
        d[i][0] = 1
        
print(d)
print(d[input])

