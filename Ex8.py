# Задача 8: Требуется определить, можно ли от шоколадки размером n
# × m долек отломить k долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).
# 3 2 4 -> yes
# 3 2 1 -> no

m = int(input('Долек по горизонтали: '))
n = int(input('Долек по вертикали: '))
k = int(input('Долек шоколадки хотите отломить: '))
if k % m == 0 or k % n == 0:
    print('Да, у Вас все получится!')
else:
    print('Нет, так не получится')