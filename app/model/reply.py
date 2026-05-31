from app.model.database import Database
from sqlite3 import Binary

class Reply:

    def criartabela():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS resposta(
            id INTEGER PRIMARY KEY,
            post_id INTEGER REFERENCES posts(id),
            titulo TEXT,
            msg TEXT,
            hora TEXT DEFAULT CURRENT_TIMESTAMP,
            midia TEXT  
        )
        ''')
        conn.commit()

    def cadastrar(postid, titulo, msg, caminho):
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('INSERT INTO resposta VALUES(NULL, ?, ?, ?, CURRENT_TIMESTAMP, ?)',(postid, titulo, msg, caminho))
        
        conn.commit()
        cursor.close()
        conn.close()

    def consultar():
        conn = Database.conectar()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM resposta')
        resultado = cursor.fetchall()
        conn.close()
        return resultado