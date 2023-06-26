"""
Запуск SQL скриптов
"""
import sqlite3

sql_file = str(input("SQL filename>>> "))

connection = sqlite3.connect('database.db')

with open('_sql/' + sql_file) as f:
    connection.executescript(f.read())

connection.commit()
connection.close()