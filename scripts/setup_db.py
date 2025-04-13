import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()


cursor.execute('''

CREATE TABLE transactions (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               date TEST,
               description TEXT,
               amount REAL,
               category TEXT
               )
               '''
               )

cursor.execute('''
CREATE TABLE goals (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               goal_name TEXT,
               target_amount REAL,
               current_amount REAL,
               target_date TEXT
               )
               ''')
conn.commit()
conn.close()

