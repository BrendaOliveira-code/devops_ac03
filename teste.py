#conectando a bibiloteca do python, memory significa que os dados serão criados na memoria, 
# só existe quando executamos o script, nao fica salvo em nenhum arquivo diferente do exercicio1
# que salva a tabela. 
import sqlite3
conn = sqlite3.connect(':memory:')

c = conn.cursor()

#criando a tabela
c.execute('''CREATE TABLE exercicio1_brenda(
                id integer,
                nome text not null,
                email text,
                primary key (id) )'''
                )

# Inserindo dados na tabela
c.execute("INSERT INTO exercicio1_brenda VALUES (1,'BRENDA OLIVEIRA','brenda@123.com')")

# Dando um select na tabela que criamos acima, a "pragma_table_info(m.name)" é uma função
# que utilizamos para descrever todos os dados de uma tabela.
c.execute('''SELECT * 
                FROM sqlite_master AS m, pragma_table_info(m.name)
                WHERE tbl_name = 'exercicio1_brenda'
            ''')

# Usar a função abaixo para printar o resultado na tela         
for row in c.fetchall():
    print('--------------- Testando a tabela --------------- ')
    print('Nomes dos campos: ', row[6])
    print('PK: ', row[10])
    print('Permissão de nulo: ', row[8])
    ## o numero está vinculado aq tabela do sqlite:
    #row[1] = nome da tabela
    #row[2] = nome da tabela
    #row[3] = rootpage
    #row[4] = script sql
    #row[5] = cid
    #row[6] = name coluna
    #row[7] = type coluna
    #row[8] = not null (0 = permite null / 1 = nao permite null)
    #row[9] = default value
    #row[10] = pk (0 = nao / 1 = sim)

# Salvar as alterações
conn.commit()

# Encerrar.
conn.close()





