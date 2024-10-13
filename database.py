import sqlite3
import bcrypt

conn =sqlite3.connect("cadastro.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Username UNIQUE  NOT NULL,
               Email VARCHAR NOT NULL,
               Password VARCHAR NOT NULL
               )
     
         
""")
def create_user(conn, cursor, username, email, password):
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        cursor.execute("""
            INSERT INTO users (Username, Email, Password)
            VALUES (?, ?, ?)
        """, (username, email, hashed_password))
        conn.commit()
        print("User created successfully!")
    except sqlite3.Error as e:
        print("Error creating user:", e)

# Connect to the database
conn = sqlite3.connect("cadastro.db")
cursor = conn.cursor()

# Create a user (replace username, email, and password with your values)
create_user(conn, cursor, "admin", "admin@example.com", "admin123")


cursor.execute("""
    CREATE TABLE IF NOT EXISTS logins (
     ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
               Username UNIQUE NOT NULL,
               Email VARCHAR NOT NULL,
               Password VARCHAR NOT NULL
               )
""")

print("Conexão de dados feita com sucessos!")











