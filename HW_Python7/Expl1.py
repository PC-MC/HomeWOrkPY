# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
# Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) 
# в каждой фразе стихотворения одинаковое. Фраза может состоять из одного слова, 
# если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
# В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам 


def rhythm(str):
    str = str.split()
    list_1 = []
    for word in str:
        count_1 = 0
        for i in word:
            if i in 'а':
                count_1 += 1
        list_1.append(count_1)
    return len(list_1) == list_1.count(list_1[0])

string = input('Введите слова через пробел разделяя слоги дефисами: ')

if rhythm(string):
    print('Парам пам-пам')
else:
    print('Пам парам')
    


# Еще вариант

# def check_vowels(phrase):
#     count = 0
#     for i in phrase:
#         if i in 'аяуюоеёэиы':
#             count += 1
#     return count


# poem = input("Введите стишок: ").lower()
# phrases = poem.split()

# count = check_vowels(phrases[0])
# has_same_vowels = True

# for i in phrases:
#     if check_vowels(i) != count:
#         has_same_vowels = False
#         break

# if has_same_vowels:
#     print('Парам пам-пам')
# else:
#     print('Пам парам')

# 1.    
# d = ['а', 'ы', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и']

# text = input("Введите стих: ") # Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. 
# # Фразы отделяются друг от друга пробелами.
# list_of_words = text.split()

# list_result = []
# for i in range(len(list_of_words)):
#     list_result.append(0)
#     for j in d:
#         list_result[i] += list_of_words[i].count(j)

# print("Количество гласных в словах:", list_result)

# def find_vowels(characteristic, objects):
#     for i in range(len(list_result) - 1):
#         if(list_result[i]) !=(list_result[i + 1]):
#             return False
#     return True

# print("Парам пам-пам") if find_vowels(list_result, list_of_words) else print("Пам парам")

# 2. 
# str_puh = 'пара-ра-рам рам-пам-папам па-ра-па-да'

# vowels = 'аоэеиыуёюя'
# def is_beat(string: str) -> str:
#     count = 0
#     for i in str_puh.split():
#         for j in i:
#             if j in vowels:
#                 count += 1
#     if count % 2 == 0:
#         return 'Парам пам-пам'
#     return 'Пам парам'

# print(is_beat(str_puh))


# 3.
# alp = "аеёиоуыэюя"
# word_sug = input().split()
# vowel_letters = [sum([True for j in word if j.lower() in alp]) for word in word_sug]

# if all(vowel_letters) and len(set(vowel_letters)) == 1:
#     print("Парам пам-пам")
# else:
#     print("Пам парам")