import csv
import mysql.connector

conn = mysql.connector.connect(
    host="ondeuai.mysql.database.azure.com",
    user="lucca",
    password="@BGqhac%Fs3@qQSt!4",
    database="pokemon",
    ssl_ca="{ca-cert filename}", 
    ssl_disabled=False,
    charset="utf8"
    )
cursor = conn.cursor()
if(conn.is_connected):
    print("Conexão bem sucedida!")
else:
    print("Conexão falhou")

def select_especie(cursor):
    query = "SELECT nome FROM especie"
    cursor.execute(query)
    output = cursor.fetchall()
    select = []
    for tupla in output:
        select.append(tupla[0])
    return select

def select_habilidade(cursor):
    query = "SELECT nome FROM habilidade"
    cursor.execute(query)
    output = cursor.fetchall()
    select = []
    for tupla in output:
        select.append(tupla[0])
    return select

def select_tipo(cursor):
    query = "SELECT nome FROM tipo"
    cursor.execute(query)
    output = cursor.fetchall()
    select = []
    for tupla in output:
        select.append(tupla[0])
    return select

count = 0
#'''
with open(r"H:\repositories\database-conception\dataset\DATASET_pokemon.csv", "r", encoding='utf-8') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Pular o cabeçalho, se houver
    
    for row in csv_data:      

        especies = select_especie(cursor)
        tipos = select_tipo(cursor)
        habilidades = select_habilidade(cursor)

        #print (f"especie: {especies}")

        # Extrair os valores dos campos
        especie_CSV = (row[3])
        tipo_1_CSV = (row[4])
        tipo_2_CSV = (row[5])
        habilidade_1_CSV = (row[10])
        habilidade_2_CSV = (row[11])
        habilidade_oculta_CSV = (row[12])

        if (especie_CSV != "") and not (especie_CSV in especies):
            try:
                query = "INSERT especie (nome, descricao) VALUES (%s, %s);"
                values = [especie_CSV, "Esta espécie ainda não tem uma descrição"]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em espécie: {e}")
        conn.commit()
        especies = select_especie(cursor)

        if (tipo_1_CSV != "") and not (tipo_1_CSV in tipos):
            try:
                query = "INSERT tipo (nome, descricao) VALUES (%s, %s);"
                values = [especie_CSV, "Este tipo ainda não tem uma descrição"]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em tipo 1: {e}")
            conn.commit()
            tipos = select_tipo(cursor)

        if (tipo_2_CSV != "") and not (tipo_2_CSV in tipos):
            try:
                query = "INSERT tipo (nome, descricao) VALUES (%s, %s);"
                values = [tipo_2_CSV, "Este tipo ainda não tem uma descrição"]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em tipo 2: {e}")
            conn.commit()
            tipos = select_tipo(cursor) 

        if (habilidade_1_CSV != "") and not (habilidade_1_CSV in habilidades):
            try:
                query = "INSERT habilidade (nome) VALUES (%s);"
                values = [habilidade_1_CSV]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em habilidade 1: {e}")
            conn.commit()
            habilidades = select_habilidade(cursor)           

        if (habilidade_2_CSV != "") and not (habilidade_2_CSV in habilidades):
            try:
                query = "INSERT habilidade (nome) VALUES (%s);"
                values = [habilidade_2_CSV]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em habilidade 2: {e}")
            conn.commit()
            habilidades = select_habilidade(cursor)  
        
        if (habilidade_oculta_CSV != "") and not (habilidade_oculta_CSV in habilidades):
            try:
                query = "INSERT habilidade (nome) VALUES (%s);"
                values = [habilidade_oculta_CSV]
                cursor.execute(query, values) 
            except Exception as e:
                    print(f"Ocorreu um erro em habilidade oculta: {e}")
            conn.commit()
            habilidades = select_habilidade(cursor) 
        
        count += 1
        print(f"{count}- Executando")

cursor.close()
conn.close()
file.close() 
print("FIM")