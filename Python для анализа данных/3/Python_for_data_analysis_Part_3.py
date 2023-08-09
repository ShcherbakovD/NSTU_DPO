"""
Прочитайте файл 'complex.txt' и построчно выведите считанные комплексные числа,
которые по модулю больше или равны определенному числу, строку "меньше" для меньших.
"""
try:
    input_arg = float(input('Введите аргумент (необходимый модуль): '))
    if input_arg <= 0: raise ValueError()
except ValueError: 
    print('Некорректное значение!')
 
else: file_txt = open("complex.txt", "r")

while True:
# Считываем строку из файла
    line_from_file = file_txt.readline()
# Прерываем цикл, если строка пустая
    if not line_from_file: break
# Убираем все пробелы 
    line = line_from_file.replace(" ", "")
# Сравниваем модули и выводим совпадения
    if abs(complex(line)) >= input_arg: 
        print(line)
    elif abs(complex(line)) < input_arg: 
        print('Меньше')

# Закрываем файл
file_txt.close