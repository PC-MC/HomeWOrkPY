# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

N = int(input("Введите размер списка: "))
A = [int(input("Введите цифру: ")) for i in range(N)]
mn, mx = int(input("Введите нижнюю границу поиска: ")), int(
    input("Введите верхнюю границу поиска: "))
arr = []
for i in range(len(A)):
    if mn <= A[i] <= mx:
        arr.append(i)
print(arr)


# Решение 2:

# def find_indexes(numbers, min_val, max_val):
#     indexes = []
#     for index, number in enumerate(numbers):
#         if min_val <= number <= max_val:
#             indexes.append(index)
#     return indexes

# numbers = [1, 3, 5, 7, 9, 2, 4, 6, 8]
# min_val = 3
# max_val = 7
# indexes = find_indexes(numbers, min_val, max_val)
# print(indexes)  # [1, 2, 3, 6, 7]



# Эталонное решение:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)

# Решение 3:

# def find_indexes(numbers, min_val, max_val):
#     indexes = []
#     for index, number in enumerate(numbers):
#         if min_val <= number <= max_val:
#             indexes.append(index)
#     return indexes

# N = int(input("Введите размер списка: "))
# A = [int(input("Введите цифру: ")) for i in range(N)]
# mn, mx = int(input("Введите нижнюю границу поиска: ")), int(
#     input("Введите верхнюю границу поиска: "))
# indexes = find_indexes(A, mn, mx)
# print(indexes)

# Решение 4:

# N = int(input("Введите размер списка: "))
# A = [int(input("Введите цифру: ")) for i in range(N)]
# mn, mx = int(input("Введите нижнюю границу поиска: ")), int(
#     input("Введите верхнюю границу поиска: "))
# for i in range(len(A)):
#     if mn <= A[i] <= mx:
#         print(i)