# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.
# 385916 -> yes

ticket_num = input('Введите номер билета: ')
left_ticket_num = int(ticket_num[0:3:1])
right_ticket_num = int(ticket_num[-1:2:-1])
sum_left = 0
while left_ticket_num >= 10:
    sum_left += left_ticket_num % 10
    left_ticket_num //= 10
sum_left += left_ticket_num

sum_right = 0
while right_ticket_num >= 10:
    sum_right += right_ticket_num % 10
    right_ticket_num //= 10
sum_right += right_ticket_num

if sum_left == sum_right:
    print ('Билет счастливый')
else:
    print('Не ешь этот билет - он не является счастливым билетом')