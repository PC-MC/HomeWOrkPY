# Задача 42: Узнать какая максимальная households в зоне минимального значения population

import pandas as bd

work = bd.read_csv('california_housing_train.csv')

answer = work.loc[work['population']<=work['population'].min()*1.1, ['households']].max()
print(answer)