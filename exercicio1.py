#conectando a bibiloteca do python, exercicio1 é o nome do arquivo ddl
import sqlite3
conn = sqlite3.connect('exercicio1.db')

c = conn.cursor()

#criando a tabela
c.execute('''CREATE TABLE exercicio1_brenda(
                id integer,
                nome text not null,
                email text)'''
                )

# Inserindo dados na tabela
c.execute("INSERT INTO exercicio1_brenda VALUES (1,'BRENDA OLIVEIRA','brenda@123.com')")

# Salvar as alterações
conn.commit()

# Encerrar.
conn.close()