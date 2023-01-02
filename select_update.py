import psycopg2
conn = psycopg2.connect(database="project", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute("""SELECT * FROM public.Agenda WHERE "id" = 1""")
registro = cur.fetchone()
print(registro)
# Atualização de um único registro
cur.execute("""UPDATE public.Agenda set "telefone" = '02188888888' where "id" = 1""")
conn.commit()
print("Registro Atualizado com sucesso!")
cur = conn.cursor()
print("Consulta depois da atualização")
cur.execute("""SELECT * FROM public.Agenda where "id" = 1""")
registro = cur.fetchone()
print(registro)
conn.commit()
print("Seleção realizada com sucesso!")
conn.close()
