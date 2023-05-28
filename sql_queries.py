import sqlite3

class Database:
    def __init__(self, database_url):
        self.connection = sqlite3.connect(database_url)
        self.cursor = self.connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS aluno (
            matricula text PRIMARY KEY,
            nome text,
            nota float    
        );
        """
        self.cursor.execute(create_table_query)

    def create(self, matricula, nome, nota):
        self.cursor.execute(f"INSERT INTO aluno VALUES ('{matricula}', '{nome}', {nota});")
        self.connection.commit()

    def read(self, matricula=None):
        if matricula:
            query = self.cursor.execute(f"SELECT * FROM aluno WHERE matricula={matricula};")
        else:
            query = self.cursor.execute(f"SELECT * FROM aluno")
        alunos = query.fetchall()
        return alunos

    def update(self, matricula, nome_entrada, nota_entrada):
        query = f"""
            UPDATE aluno
            SET nome= '{nome_entrada}', nota={nota_entrada} 
            WHERE matricula='{matricula}';
        """
        self.cursor.execute(query)
        self.connection.commit()

    def delete(self, matricula):
        query = f"DELETE FROM aluno WHERE matricula='{matricula}';"
        self.cursor.execute(query)
        self.connection.commit()
