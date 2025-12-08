from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def text():
    conn = sqlite3.connect("blog.db")
    return conn

def word():
    conn = text()
    conn.execute("""CREATE TABLE IF NOT EXISTS posts (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 title TEXT NOT NULL,
                 content TEXT NOT NULL,
                 created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)""")
    conn.commit()
    conn.close()

if __name__ == "__main__":
    word()
    app.run(debug=True)
