# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*

# 385916 -> yes
# 123456 -> no

# Можно сделать проверку на четность и дополнить программу чтобы она люьой четный билетик проверяла, 
# но у меня мало времени на занятия и так не успеваю ничего.

n = int(input("Введите номер вашего билета: "))
c = 0
sum = 0
sum2 = 0
if 99999 < n < 1000000:
    if n > 0:
        while n > 0 and c < 3:
            x = n % 10
            sum2 = sum2 + x
            n = n // 10
            c = c + 1
        while n > 0 and c < 6:
            y = n % 10
            sum = sum + y
            n = n // 10
            c = c + 1
    if sum == sum2:
        print("У вас счастливый билетик!")
    else:
        print("В этот раз не повезло.")
else:
    print("В этот раз не повезло.")   