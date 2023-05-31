# Задача 40 Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)


import pandas as bd
                                                                              
work = bd.read_csv('california_housing_train.csv')

answer = work.loc[work['population'] <= 500, ['median_house_value']].median()
print(answer)