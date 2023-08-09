"""
Используя библиотеки math, cmath и time сравните скорость вычисления 
квадратного корня, синуса и логарифма 1000000 раз из введённого пользователем числа. 
Алгоритм должен содержать проверку корректности входных данных. 
Результаты приведите в простой таблице.
"""
# Подключаем необходимые библиотеки
import math as m
import cmath as cm
import time

# Проверяем корректность вводимого аргумента
try:
    a = float(input('Введите аргумент: '))
    if a <= 0: raise ValueError()
except ValueError:
    print('Некорректное значение!')
 
else:
    print('Аргумент принят!')
# Выполняем рассчет времени выполения с помощью функции tm 
    n = 1000000
    def tm(fn):
        st = time.time()
        # n-раз выполняем расчёт времени выполнения функции
        for i in range(n): x = fn
        return (str(round(time.time() - st, 6)))
 
    print('\nВремя выполнения функций:')
    print(f'sin({a}) в math: {tm(m.sin(a))} в cmath: {tm(cm.sin(a))}')
    print(f'cos({a}) в math: {tm(m.cos(a))} в cmath: {tm(cm.cos(a))}')
    print(f'sqrt({a}) в math: tm(m.sqrt(a)) в cmath: {tm(cm.sqrt(a))}')
    print(f'log({a}) в math: tm(m.log(a)) в cmath: {tm(cm.log(a))}')