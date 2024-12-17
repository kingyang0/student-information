import sqlite3

# 连接到数据库
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# 创建表
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_number TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    department TEXT,
    graduation_status TEXT,
    employment TEXT
);
""")

# 提交更改并关闭连接
conn.commit()
conn.close()

print("表已成功创建！")