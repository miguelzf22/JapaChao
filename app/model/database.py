import sqlite3
class Database:
    def conectar():
        conn = sqlite3.connect('database.db')
        return conn