# Подключил необходимые библиотеки 
import sqlite3 as sql
import time

# 1.Откройте базу данных 'ABD.db' с использованием библиотеки sqlite.

# Создаём пустой список, в который циклом пропишем значения

conn = sql.connect('ABD.db')
cursor = conn.cursor()

#2.Выведите названия всех таблиц.

cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(f'\nColumns in ABD.db:{cursor.fetchall()}')

#3.Выведите все записи из таблицы 'Instruments'.
    
cursor.execute("SELECT * FROM Instruments")
print(f'\nColumns in Instruments table:{cursor.fetchall()}')
  
#4.Выберите все сделки по инструменту  'IRAO'  с ценой в диапазоне 4.9-5.0 и подсчитайте их количество. 
cursor.execute("SELECT id FROM Instruments WHERE instrumentName = 'IRAO'")
massive_IRAO = cursor.fetchone()
cursor.execute("SELECT COUNT(*) FROM Trades WHERE price BETWEEN 4.9 AND 5.0 AND instrumentId = (?)", massive_IRAO)
print (f'\nCount the IRAO 4.9-5.0: {cursor.fetchone()[0]}') 

#5.Из этих сделок выберите все сделки, которые были совершены в первой половине дня и подсчитайте их количество.
cursor.execute("SELECT COUNT(*) FROM  (SELECT * FROM Trades WHERE price BETWEEN 4.9 AND 5.0 AND instrumentId = ($s)) WHERE traded%86400 BETWEEN 0 AND 43200;",(massive_IRAO) )
print (f'\nCount the IRAO 4.9-5.0 between 0:00 and 12:00: {cursor.fetchone()[0]}') 
conn.rollback()  
      
#6.Вставьте новый инструмент с произвольными идентификатора рынка и бумаги в таблицу Instruments.
new_data_instruments = [2022,'NSTU_ABD','NSTU_IRAO']
cursor.execute('''INSERT INTO Instruments VALUES (?,?,?);''', new_data_instruments)

#7.Добавьте сделку с произвольными параметрами для этого инструмента. Закройте и сохраните базу.
# она отвечает за сброс 29 строки 
unix_time = (int(time.time()))
new_data_trades = [(new_data_instruments[0]),3,2222,3333,(unix_time),5555,6666]
cursor.execute('''INSERT INTO Trades VALUES (?,?,?,?,?,?,?);''', new_data_trades)
conn.commit()
cursor.close()