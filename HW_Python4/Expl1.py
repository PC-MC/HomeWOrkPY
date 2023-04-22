# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

s = w = []
n = int(input("Введите количество элементов в первом наборе чисел: "))
while n > 0:
    s.append(int(input("Введите элемент первого набора чисел: ")))
    n -= 1

m = int(input("Введите количество элементов во втором наборе чисел: "))
while m > 0:
    w.append(int(input("Введите элемент второго набора чисел: ")))
    m -= 1

w, s = set(w), set(s)
array = []
for i in s:
    for j in w:
        if i == j:
            array.append(i)
print(sorted(array))

# Эталонное решение:
# mol = [int(x) for x in input().split()]
# n = mol[0]
# m = mol[1]
# set_1 = set()
# set_2 = set()
# list_1 = list()
# a = [int(x) for x in input().split()]
# k = set(a)
# for i in k:
#     set_1.add(i)
# b = [int(x) for x in input().split()]
# k1 = set(b)
# for i in k1:
#     set_2.add(i)
# lok = set_1 & set_2
# kool = list(lok)
# kool.sort()
# for i in kool:
#     print(i, end=' ')

