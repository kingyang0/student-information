import sqlite3

def add_student(student_number, name, age, department, graduation_status, employment):
    conn = sqlite3.connect("/Users/mac/Desktop/工程实践3/database.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (student_number, name, age, department, graduation_status, employment) VALUES (?, ?, ?, ?, ?, ?)",
                   (student_number, name, age, department, graduation_status, employment))
    conn.commit()
    conn.close()

def delete_student(student_id):
    conn = sqlite3.connect("/Users/mac/Desktop/工程实践3/database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()

def update_student(student_id, **kwargs):
    conn = sqlite3.connect("/Users/mac/Desktop/工程实践3/database.db")
    cursor = conn.cursor()
    columns = ', '.join([f"{key} = ?" for key in kwargs.keys()])
    values = list(kwargs.values()) + [student_id]
    cursor.execute(f"UPDATE students SET {columns} WHERE student_id = ?", values)
    conn.commit()
    conn.close()

def search_students(keyword):
    conn = sqlite3.connect("/Users/mac/Desktop/工程实践3/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE student_number LIKE ? OR name LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    result = cursor.fetchall()
    conn.close()
    return result

def list_all_students():
    conn = sqlite3.connect("/Users/mac/Desktop/工程实践3/database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()
    conn.close()
    return result
