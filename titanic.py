import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_parquet('titanic.parquet')
f.to_csv('titanic.csv')

df = pd.read_csv('titanic.csv')

a = df.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

surv = a.div(a.sum(axis=1), axis=0) * 100 

surv.plot(kind='bar', stacked=True)

plt.title('Выживаемость пассажиров от класса') 
plt.xlabel('Класс') 
plt.ylabel('% выживаемости') 
plt.xticks(rotation=0)
plt.legend(['Не выжил', 'Выжил']) 
plt.tight_layout()

plt.show()