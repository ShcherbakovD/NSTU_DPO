'''
Для набора значений в приложенном файле data.xlsх 
Провести аппроксимацию данных функцией вида: 
exp(−(x/s)2). 
По результатам аппроксимации определить среднеквадратическое отклонение s. 
Построить графики.
Определить простое среднее значение функции в интервале значений х. 
Вычислить производную и интеграл от функции, значения которой определены в столбце у. 
Определить область экстремума. 
'''
# Импортируем необходимые библиотеки и модули 
from scipy.optimize import curve_fit,  root
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd
# Часть первая - график точек из датасета
# Отркываем файл
excel_data_df = pd.read_excel('data.xlsx')
# Копируем прочитанные данные
data = excel_data_df.copy()
# Выводим скопированные данные
print(excel_data_df)
# Присваем спискам значения столбцов
values_x = data['x']
values_y = data['y']

# Аппроксимация функцией 
def mapping(x, s): 
    return np.exp(-((x)/s)**2)
args, _  = curve_fit(mapping, values_x, values_y) 
s = args[0]
print("Полином функции s : ", s)
y_fit = mapping(values_x, s)
# Строим график функции и точек из датасета
plt.figure(figsize = (20,10))
plt.plot(values_x, values_y, 'ro', label="y from dataset") 
plt.plot(values_x, y_fit, linewidth = 5, label="y(x)") 
plt.xlabel('x') 
plt.ylabel('y') 
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig('y(x)_and_dataset.png')
plt.grid(True) 

# Задаём символическую переменную
x = sp.Symbol('x')
# Задаём символическую функцию
y = sp.exp(-(x/s)**2)
# Находим производную от функции y
diff_y = sp.diff(y, x)
# Находим интеграл от функции diff_y
integ_diff_y = sp.integrate(diff_y, x)
# Находим интеграл от функции y
integ_y = sp.integrate(y, x)

print(f'Производная функции {y} : {diff_y}')
print(f'Интеграл функции {diff_y} : {integ_diff_y}')
print(f'Интеграл функции {y} : {integ_y}')
print(f'Среднеарифмитическое по функции {np.mean(y_fit)}')
print(f'Среднеарифмитическое по x {np.mean(values_x)}')
print(f'Среднеарифмитическое по y {np.mean(values_y)}')
print(f'Среднеквадратическое по функции {np.std(y_fit)}')
print(f'Среднеквадратическое по y {np.std(values_y)}')

# Находим производную, как скорость изменения функции
y_analitic = -16.6929468238358*values_x*np.exp(-8.34647341191788*values_x**2)
dy = np.zeros(values_y.shape,float)
dy[0:-1] = np.diff(values_y)/np.diff(values_x)
plt.figure(figsize = (20,10))
plt.figure(figsize = (20,10))
plt.plot(values_x,values_y,  label="Dataset")
plt.plot(values_x, y_analitic,'o', label="Diff_Exact") 
plt.plot(values_x,dy,'-o', label="Diff_Numerical") 
plt.legend()
plt.xlim([-1,1]); plt.ylim([-5,5])
plt.savefig('Numerical_Differentiation.png')


# Нажодим интеграл, как площадь кривой фигуры 
Trapz_Rule = np.trapz(values_y,values_x)
print("Интеграл, как площадь криволинейной фигуры, равен ", Trapz_Rule)
plt.figure(figsize = (20,10))
plt.plot(values_x, values_y)
plt.axhline(color="black")
plt.fill_between(values_x, values_y)
plt.legend()
plt.savefig('Numerical Integration.png')


def f(x):
    return -16.6929468238358*x*np.exp(-8.34647341191788*x**2)
# Находим нули функции
x0 = 0
sol = root(f, x0, method='lm')
# Строим график производной с нулями функции
plt.figure(figsize = (20,10))
plt.plot(values_x, f(values_x), linewidth = 5, label="y(x)") 
plt.scatter(sol.x, f(sol.x),c = 'r', linewidths = 6 , label="y(x) = 0")
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xlabel('x') 
plt.ylabel('y') 
plt.savefig('diff(y(x))_and_zero.png')





