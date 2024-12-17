from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

def register(username, password, role="user"):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    hashed_password = generate_password_hash(password)
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, hashed_password, role))
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()

def login(username, password):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username=?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result and check_password_hash(result[0], password):
        return True
    return False
