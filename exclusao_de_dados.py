"""
Excluindo registro de uma tabela
"""
import psycopg2
conn = psycopg2.connect(database="project", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""DELETE FROM Public.Agenda WHERE "id" = 1""")
conn.commit()
cont = cur.rowcount  # rowcount retorna a quantidade de registros excluídos
print(cont, "Registro excluído com sucesso!")
print("Exclusão realizada com sucesso!")
conn.close()