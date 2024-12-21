import sqlite3

conn = sqlite3.connect('database.db')
print("Connected to database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT, high_score INT,student_number TEXT UNIQUE)')
conn.execute('CREATE TABLE IF NOT EXISTS  author (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, title TEXT)')
conn.execute('CREATE TABLE IF NOT EXISTS questions (id INTEGER PRIMARY KEY AUTOINCREMENT, questions TEXT, options TEXT, correct_answer TEXT)')
print("Created table successfully!")
conn.close()
