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



#'''
#Nesta classe salvaramos os dados cindos do csv para trata-los.
class PokemonCSV:
    def __init__(self, id, name, categoria, especie, tipo_1, tipo_2, peso, ataque, defesa, velocidade, habilidade_1, habilidade_2, habilidade_oculta):
        self.id = id
        self.nome = name
        self.categoria = categoria
        self.especie = especie
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.peso = peso
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.habilidade_1 = habilidade_1
        self.habilidade_2 = habilidade_2
        self.habilidade_oculta = habilidade_oculta
    
    def imprimir_atributos(self):
        print("Atributos do Pokemon:")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Espécie: {self.especie}")
        print(f"Tipo 1: {self.tipo_1}")
        print(f"Tipo 2: {self.tipo_2}")
        print(f"Peso: {self.peso}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        print(f"Velocidade: {self.velocidade}")
        print(f"Habilidade 1: {self.habilidade_1}")
        print(f"Habilidade 2: {self.habilidade_2}")
        print(f"Habilidade Oculta: {self.habilidade_oculta}")

#Nesta classe o pokemon tem seus atributos já tratados.
class Pokemon:
    def __init__(self, id=None, name=None, categoria=None, especie=None, tipo_1=None, tipo_2=None, peso=None, ataque=None, defesa=None, velocidade=None, habilidade_1=None, habilidade_2=None, habilidade_oculta=None):
        self.id = id
        self.nome = name
        self.categoria = categoria
        self.especie = especie
        self.tipo_1 = tipo_1
        self.tipo_2 = tipo_2
        self.peso = peso
        self.ataque = ataque
        self.defesa = defesa
        self.velocidade = velocidade
        self.habilidade_1 = habilidade_1
        self.habilidade_2 = habilidade_2
        self.habilidade_oculta = habilidade_oculta

    def imprimir_atributos(self):
        print("Atributos do Pokemon:")
        print(f"ID: {self.id}")
        print(f"Nome: {self.nome}")
        print(f"Categoria: {self.categoria}")
        print(f"Espécie: {self.especie}")
        print(f"Tipo 1: {self.tipo_1}")
        print(f"Tipo 2: {self.tipo_2}")
        print(f"Peso: {self.peso}")
        print(f"Ataque: {self.ataque}")
        print(f"Defesa: {self.defesa}")
        print(f"Velocidade: {self.velocidade}")
        print(f"Habilidade 1: {self.habilidade_1}")
        print(f"Habilidade 2: {self.habilidade_2}")
        print(f"Habilidade Oculta: {self.habilidade_oculta}")

with open(r"H:\repositories\database-conception\dataset\DATASET_pokemon1.csv", "r", encoding='utf-8') as file:
    csv_data = csv.reader(file)
    next(csv_data)  # Pular o cabeçalho, se houver
    
    for row in csv_data:
        # Extrair os valores dos campos
        pokemon = Pokemon()
        pokemonCSV = PokemonCSV(
            id=int(row[0]),
            name=row[1],
            categoria=row[2],
            especie=row[3],
            tipo_1=row[4],
            tipo_2=row[5],
            peso=(row[6]),
            ataque=(row[7]),
            defesa=(row[8]),
            velocidade=(row[9]),
            habilidade_1=(row[10]),
            habilidade_2=(row[11]),
            habilidade_oculta=(row[12])
        )

        pokemon.id = pokemonCSV.id
        pokemon.nome = pokemonCSV.nome
        pokemon.peso = pokemonCSV.peso
        pokemon.ataque = pokemonCSV.ataque
        pokemon.defesa = pokemonCSV.defesa
        pokemon.velocidade = pokemonCSV.velocidade

        try:               
            query = "SELECT pokemon_id FROM pokemon WHERE pokemon_id = %s"
            print(f"Pokemon.id: {pokemonCSV.id}")
            values = [pokemonCSV.id]
            cursor.execute(query, values)
            existe = cursor.fetchone()
            cursor.nextset()
        except Exception as e:
            print(f"Ocorreu em verificar a existência do ID: {e}")

        if (existe == None):

            try:               
                query = "SELECT especie_id FROM especie WHERE nome = %s"
                values = [pokemonCSV.especie]
                cursor.execute(query, values)
                pokemon.especie = cursor.fetchone()[0]
                cursor.nextset()
            except Exception as e:
                print(f"Ocorreu um erro em SELECT espécie: {e}")


            try:
                query = "SELECT categoria_id FROM categoria WHERE nome = %s"
                values = [pokemonCSV.categoria]
                cursor.execute(query, values)
                pokemon.categoria = cursor.fetchone()[0]
                cursor.nextset()   
            except Exception as e:
                print(f"Ocorreu um erro em SELECT categoria: {e}")


            try:
                query = "SELECT tipo_id FROM tipo WHERE nome = %s"
                values = [pokemonCSV.tipo_1]
                cursor.execute(query, values)
                pokemon.tipo_1 = cursor.fetchone()[0]
                cursor.nextset()
            except Exception as e:
                print(f"Ocorreu um erro em SELECT tipo 1: {e}")

            try:    
                if(pokemonCSV.tipo_2 != ""):
                    query = "SELECT tipo_id FROM tipo WHERE nome = %s"
                    values = [pokemonCSV.tipo_2]
                    cursor.execute(query, values)
                    pokemon.tipo_2 = cursor.fetchone()[0]
                    cursor.nextset()   
            except Exception as e:
                print(f"Ocorreu um erro em SELECT tipo 2: {e}")


            try:
                if(pokemonCSV.habilidade_1 != "" ):
                    query = "SELECT habilidade_id FROM habilidade WHERE nome = %s"
                    values = [pokemonCSV.habilidade_1]
                    cursor.execute(query, values)
                    pokemon.habilidade_1 = cursor.fetchone()[0]
                    cursor.nextset()        
            except Exception as e:
                print(f"Ocorreu um erro em SELECT habilidade 1: {e}")

            try:
                if(pokemonCSV.habilidade_2 != "" ):
                    query = "SELECT habilidade_id FROM habilidade WHERE nome = %s"
                    values = [pokemonCSV.habilidade_2]
                    cursor.execute(query, values)
                    pokemon.habilidade_2 = cursor.fetchone()[0]
                    cursor.nextset()  
            except Exception as e:
                print(f"Ocorreu um erro em SELECT habilidae 2: {e}")
            

            try:
                if(pokemonCSV.habilidade_oculta != "" ):
                    query = "SELECT habilidade_id FROM habilidade WHERE nome = %s"
                    values = [pokemonCSV.habilidade_oculta]
                    cursor.execute(query, values)
                    pokemon.habilidade_oculta = cursor.fetchone()[0]
                    cursor.nextset()
            except Exception as e:
                print(f"Ocorreu um erro em SELECT habilidade oculta: {e}")

                    
            query = "INSERT INTO pokemon (pokemon_id, nome, peso, valor_ataque, valor_defesa, velocidade_media, especie_especie_id, categoria_categoria_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = [pokemon.id, pokemon.nome, pokemon.peso, pokemon.ataque, pokemon.defesa, pokemon.velocidade, pokemon.especie, pokemon.categoria]
            cursor.execute(query, values)
            conn.commit()


            # Nível primário: nivel = 1;
            query = "INSERT INTO pokemon_tipo (pokemon_pokemon_id, tipo_tipo_id, nivel) VALUES (%s, %s, %s)"
            values = [pokemon.id, pokemon.tipo_1, 1]
            cursor.execute(query, values)
            conn.commit()

            # Nível secundário: nivel = 0;
            if (pokemon.tipo_2):
                query = "INSERT INTO pokemon_tipo (pokemon_pokemon_id, tipo_tipo_id, nivel) VALUES (%s, %s, %s)"
                values = [pokemon.id, pokemon.tipo_2, 0]
                cursor.execute(query, values)
                conn.commit()

            # Estruturas condicionais para criar tabelas de associação se nescesáirio
            if (pokemon.habilidade_1):
                query = "INSERT INTO pokemon_habilidade (pokemon_pokemon_id, habilidade_habilidade_id, oculta) VALUES (%s, %s, %s)"
                values = [pokemon.id, pokemon.habilidade_1, None]
                cursor.execute(query, values)
                conn.commit()


            if (pokemon.habilidade_2):
                query = "INSERT INTO pokemon_habilidade (pokemon_pokemon_id, habilidade_habilidade_id, oculta) VALUES (%s, %s, %s)"
                values = [pokemon.id, pokemon.habilidade_2, None]
                cursor.execute(query, values)
                conn.commit()

            if (pokemon.habilidade_oculta):
                query = "INSERT INTO pokemon_habilidade (pokemon_pokemon_id, habilidade_habilidade_id, oculta) VALUES (%s, %s, %s)"
                values = [pokemon.id, pokemon.habilidade_oculta, 1]
                cursor.execute(query, values)
                conn.commit()
                

            print(".........................................................")

            pokemon.imprimir_atributos()

            print(".........................................................")


            print("---------------------------------------------------------")
            print("---------------------------------------------------------")
            print("\n")

cursor.close()
conn.close()
file.close()
#'''