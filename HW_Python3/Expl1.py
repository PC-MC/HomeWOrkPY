# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai (можно использовать псевдогенерацию). 
# Последняя строка содержит число X.

# *Пример:*

# 5
#     7 -2 3 5 1
#     3
#     -> 1


n = input("Введите элементы массива через пробел: ")
array = n.split()
for i in range(len(array)):
    array[i] = int(array[i])
x =int(input("Ведите число: "))
count = 0 
for element in array:
    if element == x:
        count += 1
print("Массив: ", array)
print("Число", x, "встречается в массиве", count, "раз(а).")