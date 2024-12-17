import sqlite3

def init_db():
    conn = sqlite3.connect('/Users/mac/Desktop/工程实践3/database.db')
    cursor = conn.cursor()
    
    # 创建用户表
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        role TEXT NOT NULL
    )''')
    
    # 创建学生表
    cursor.execute('''CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_number TEXT NOT NULL UNIQUE,
        name TEXT NOT NULL,
        age INTEGER,
        department TEXT,
        graduation_status TEXT,
        employment TEXT
    )''')
    
    conn.commit()
    conn.close()

# 初始化数据库
init_db()
