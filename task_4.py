# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

x = int(input('Введите номер четверти плоской системы координат: '))
if x == 1 :
    print('Диапазон возможных координат точек в 1-ой четверти: x > 0 и y > 0')
elif x == 2 :
    print('Диапазон возможных координат точек в 2-ой четверти: x < 0 и y > 0')
elif x == 3 :
    print('Диапазон возможных координат точек в 3-ей четверти: x < 0 и y < 0')
elif x == 4 :
    print('Диапазон возможных координат точек в 4-ой четверти: x > 0 и y < 0')
else: print('Введите число в дипазоне от 1 до 4 включительно !')