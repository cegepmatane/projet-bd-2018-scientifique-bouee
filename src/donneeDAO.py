import sqlite3
import datetime
import json


def insererValeur(temperatureAir,temperatureEau,directionVent,kilometrageVent,hauteurMaximum,vagueMoyenne,periodeVague,humidite,rafales,salaniteEau,densiteeEau):
    
    connection = sqlite3.connect("bouee.db") #connection a la table bouee de la bd sqlite
    curseur = connection.cursor()
    curseur.execute('''INSERT INTO donneeBouee(temperatureAir,temperatureEau,directionVent,vitesseVent,hauteurMaximum,vagueMoyenne,periodeVague,humidite,rafales,saliniteEau,densiteeEau) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',(temperatureAir,temperatureEau,directionVent,kilometrageVent,hauteurMaximum,vagueMoyenne,periodeVague,humidite,rafales,salaniteEau,densiteeEau))

    connection.commit()
    connection.close()
        
        
def recupererValeur():

    connection = sqlite3.connect("bouee.db") #connection a la table bouee de la bd sqlite
    print("connecte")

    connection.row_factory = sqlite3.Row

    curseur = connection.cursor()
    resultat = curseur.execute('''SELECT temperatureAir,temperatureEau,directionVent,vitesseVent,hauteurMaximum,vagueMoyenne,periodeVague,humidite,rafales,saliniteEau,densiteeEau FROM donneeBouee''').fetchall()

    """for row in curseur:
    row[0] returns the first column in the query (name), row[1] returns email column.
        print('{0} : {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}, {9}, {10}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]))"""

    curseur.execute('''DELETE FROM donneeBouee''')
    connection.commit()
    connection.close()

    donneeJson = ""
    donneeJson = json.dumps([dict(ix) for ix in resultat] )
    print(donneeJson)

