import sqlite3

class Database:
    def __init__(self, database_url):
        self.connection = sqlite3.connect(database_url)
        self.cursor = self.connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS aluno (
            id text PRIMARY KEY,
            produto text,
            preco int    
        );
        """
        self.cursor.execute(create_table_query)

    def create(self, id, produto, preco):
        self.cursor.execute(f"INSERT INTO aluno VALUES ('{id}', '{produto}', {preco});")
        self.connection.commit()

    def read(self, id=None):
        if id:
            query = self.cursor.execute(f"SELECT * FROM aluno WHERE id={id};")
        else:
            query = self.cursor.execute(f"SELECT * FROM aluno")
        alunos = query.fetchall()
        return alunos

    def update(self, id, produto_entrada, preco_entrada):
        query = f"""
            UPDATE aluno
            SET produto= '{produto_entrada}', preco={preco_entrada} 
            WHERE id='{id}';
        """
        self.cursor.execute(query)
        self.connection.commit()

    def delete(self, id):
        query = f"DELETE FROM aluno WHERE id='{id}';"
        self.cursor.execute(query)
        self.connection.commit()
