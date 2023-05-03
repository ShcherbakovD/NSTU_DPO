# Подключил необходимые библиотеки 
import sqlite3 as sql
import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Открываем БД
conn = sql.connect('ABD-VKR.db')
cursor = conn.cursor()
# Делаем вывод списка по классу инструментов с исключением повторяющихся значений
cursor.execute("SELECT DISTINCT className FROM Instruments")
all_id = cursor.fetchall()
# Выводим результат запроса
name = [x[0] for x in all_id]
print(name)
txt = input("Введите : ")
target_class = txt
cursor.execute("SELECT instrumentName  FROM Instruments WHERE className = (?)", [target_class])
massive_NAME = cursor.fetchall()
name = [x[0] for x in massive_NAME]
print(name)
txt = input("Введите : ")
target_instrument = txt
cursor.execute("SELECT id  FROM Instruments WHERE className = (?) AND instrumentName = (?)", [target_class, target_instrument],)
target_ID = cursor.fetchall()
print(*target_ID)
cursor.execute("SELECT traded FROM Trades WHERE instrumentId = (?)", target_ID[0])
time_name = cursor.fetchall()
cursor.execute("SELECT price FROM Trades WHERE instrumentId = (?)", target_ID[0])
y = cursor.fetchall()
for items in time_name:
    items = pd.to_datetime(items, unit='s')
    print (items[0])

cursor.close()