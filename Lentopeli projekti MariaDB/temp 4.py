
# Importit
import mysql.connector
import random
from geopy import distance


# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}

yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

def game_values(game_id):
    #Ottaa game:id ja palauttaa game taulun tiedot listana.

    values = []

    sql = f"SELECT * FROM game WHERE game.id = '{game_id}';"
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    for tuple in sql_list:
        for n in range(0, 9):
            values.append(tuple[n])

    #Palautetaan lista
    return values





###########################################

game_id = 35
game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)

game_id = 41


sql =  f" INSERT INTO visited (game_id, ident) VALUES ('{game_id}', '{game_location}') "
print(sql)

kursori.execute(sql)



#sql_read = kursori.fetchall()
#print(sql_read)


yhteys.commit()

