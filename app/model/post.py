from app.model.database import Database
from sqlite3 import Binary

class Post:

    def criartabela():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS posts(
            id INTEGER PRIMARY KEY,
            titulo TEXT,
            msg TEXT,
            hora TEXT DEFAULT CURRENT_TIMESTAMP,
            midia TEXT  
        )
        ''')
        conn.commit()

    def cadastrar(titulo, msg, caminho):
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO posts VALUES(NULL, ?, ?, CURRENT_TIMESTAMP, ?)',(titulo, msg, caminho))
        
        conn.commit()
        cursor.close()
        conn.close()

    def consultar():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM posts')
        resultado = cursor.fetchall()
        conn.close()
        return resultado