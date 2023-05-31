# Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), 
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. 
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. 
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как,
# например, у операции умножения.

# *Пример:*

# **Ввод:** `print_operation_table(lambda x, y: x * y) ` 
# **Вывод:**
# 1 2 3 4 5 6

# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36



def print_operation_table(operation, num_rows, num_columns):
    for i in range(1, num_rows + 1):
        list_1 = []
        for j in range(1, num_columns + 1):
            list_1.append(operation(i, j))
            if list_1[-1] > 9:
                print(f"{list_1[-1]}", end="  ")
            else:
                print(f"{list_1[-1]}", end="   ")
        print(end="\n")


r = int(input("Введите количество строк: "))
c = int(input("Введите количество столбцов: "))
print_operation_table(lambda x, y: x*y, r, c)


# 1.
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         print()
#         for j in range(1, num_columns + 1):
#             print('''{:<3}'''.format(operation(i,j)), end=" ")
# print_operation_table(lambda x, y: x * y)


# 2.
# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for x in range(1, num_rows + 1):
#         lists = []
#         for y in range(1, num_columns + 1):
#             num = operation(x, y)
#             lists.append(num)
#         print(*[str(x) for x in lists])

# print_operation_table(lambda x, y: x * y)