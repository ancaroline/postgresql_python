import psycopg2

conn = psycopg2.connect(database="project", user="postgres", password="1234", host="127.0.0.1", port="5432")
print("Conexão com o Banco de Dados aberta com sucesso!")
cur = conn.cursor()
cur.execute('''INSERT INTO public.Agenda ("id", "nome", "telefone") 
                VALUES (1, 'João Henrique', '332352214')''')
conn.commit()
print("Inserção realizada com sucesso!")
conn.close()