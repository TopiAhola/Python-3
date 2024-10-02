


def distance( origin, destination ):
# Laskee kahden kentän välisen etäisyyden. Syöte on kenttien ident-koodi. Antaa tuloksen kilometreinä kokonaislukuna.

     #Haetaan koordinaatit
    sql1= f"select longitude_deg, latitude_deg from kentat where ident ='{origin}'  "
    sql2= f"select longitude_deg, latitude_deg from kentat where ident ='{destination}' "

    kursori.execute(sql1)
    tulos1 = kursori.fetchall()
    kursori.execute(sql2)
    tulos2 = kursori.fetchall()
    #kursori.close()

    #lasketaan etäisyys, muunnetaan kokonaisluvuksi
    dist = int(distance.distance(tulos1, tulos2).km)

    return dist


def random_location():
    #Antaa satunnaisen kentan ident-koodin

    #Haetaan kenttien ident.koodit listaan:
    sql = f"SELECT ident FROM kentat;"
    kursori.execute(sql)
    list = kursori.fetchall()
    #kursori.close()

    #Arvotaan kenttä väliltä 0, listan pituus-1
    n = random.randint(0, len(list)-1)

    #Karsitaan erikoimerkit pois listaobjektista
    location = str(list[n])
    location = location.replace("('", "")
    location = location.replace("',)", "")

    #Palautetaan ident-koodi
    return location


def new_game():
    # Luo pelaajan ja tavoitteet ja syöttää ne tietokantaan.
    # Palauttaa pelaajan game_id tietokannasta.
    # Palauttaa tavoitteet listana goal_list



    name = input("Pelaajan nimi: ")
    location = random_location()
    money = 1500
    co2 = 0
    money_gained = 0
    money_spent = 0
    distance = 0
    flights = 0

    sql_game = (f"INSERT INTO game(name, location, money, co2, money_gained, money_spent, distance, flights) "
            f"VALUES ('{name}', '{location}', '{money}', '{co2}', '{money_gained}', '{money_spent}', '{distance}', '{flights}' )")
    kursori.execute(sql_game)
    yhteys.commit()


    #Haetaan uusimman pelin id:
    sql2 = f"SELECT id FROM game WHERE id IN (SELECT max(id) FROM game)"
    kursori.execute(sql2)
    sql_tuple = kursori.fetchone()
    #kursori.close()
    game_id =sql_tuple[0]

    # Arvotaan tavoitteet
    goal_list = []
    while len(goal_list) < 5:
        kentta = random_location()
        if kentta != location and kentta not in goal_list:
            goal_list.append(kentta)

    for kentta in goal_list:
        sql_goal = (f"INSERT INTO goal(game_id, ident, reached)"
                    f"VALUES('{game_id}', '{kentta}', '0')   ")
        kursori.execute(sql_goal)
        yhteys.commit()


    return game_id


def goal_reached(game_id):
    #Hakee saavutettujen tavoitteiden totuusarvot tietokannasta.
    #Palauttaa True jos kaikki arvot != 0
    goal_bool = False


    sql = f"SELECT reached FROM goal WHERE game_id = '{game_id}';"
    kursori.execute(sql)
    sql_list = kursori.fetchall()

    #Muutetaan SQL tuplet 0 tai 1 arvoksi
    bool_values = []
    for rivi in sql_list:
        bool_values.append(rivi[0])

    if 0 not in bool_values:
        goal_bool = True

    print(bool_values)
    return goal_bool

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

def show_goals(game_id):
    #Kertoo pelaajan tavoitteet ja missä on käynyt.

    sql = f" SELECT kentat.name, kentat.country_fi FROM kentat RIGHT JOIN goal ON goal.ident = kentat.ident WHERE goal.game_id = '{game_id}'  "
    kursori.execute(sql)
    sql_list = kursori.fetchall()
    goal_list = []
    for tuple in sql_list:
        goal_list.append(tuple)

    print(f"\nSinulla on {len(goal_list)} tavoitetta jäljellä: \n")
    for tuple in goal_list:
        print(f"{tuple[0]}, {tuple[1]}")

def show_locations(game_id):



## PÄÄOHJELMA

# Importit
import mysql.connector
import random
from geopy import distance

# Yhteys tietokantaan
parametrit = {"host": 'localhost', 'database': 'flight_game', 'user': 'game', 'password': '',
              "collation": "latin1_swedish_ci"}
yhteys = mysql.connector.connect(**parametrit)
kursori = yhteys.cursor()

'''
# Muuttujat, haetaan tietokannasta

game_values lista sisältää:
[0] game_id 
[1] game_name 
[2] game_location
[3] game_money
[4] game_co2
[5] game_money_gained
[6] game_money_spent
[7] game_distance
[8] game_flights

Muut globaalit muuttujat:
goal_list -lista tavoitekenttien ident-koodeista

'''
#Peli alkaa



# Luodaan uusi peli:
# Myöhemmin voidaan lisätä valitarakenne jolla voi ladata vanhan pelin, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights, goal_list = new_game()
game_id = new_game()
game_id, game_name, game_location, game_money, game_co2, game_money_gained, game_money_spent, game_distance, game_flights = game_values(game_id)


show_goals(game_id)

## Pelin toistorakenne:

#while goal_reached(game_id) != True:


