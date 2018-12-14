import random
import time
import json
import donneeDAO

running=True

#boucle generant 10 donnees par seconde
while running:
    """donnee=[]
    donnee.append(("\"temperatureAir\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"temperatureEau\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"directionVent\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"kilometrageVent\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"hauteurMaximum\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"vagueMoyenne\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"periodeVague\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"humidite\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"rafales\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"salaniteEau\"",random.uniform(0,100))) #generation de salinite aleatoire en %
    donnee.append(("\"densiteeEau\"",random.uniform(0,100))) #generation de difraction aleatoire en % 
   
    stringFormatee="{"
    for i in donnee:
        stringFormatee+=str(i[0])
        stringFormatee+=":"
        stringFormatee+="\""+str(i[1])+"\""
        stringFormatee+=","
    
    stringFormatee=stringFormatee[:-1]
    stringFormatee+="}"
    print(stringFormatee)"""

    temperatureAir = random.uniform(-10,40)
    temperatureEau = random.uniform(-10,40)
    directionVent = random.uniform(-10,40)
    kilometrageVent = random.uniform(-10,40)
    hauteurMaximum = random.uniform(-10,40)
    vagueMoyenne = random.uniform(-10,40)
    periodeVague = random.uniform(-10,40)
    humidite = random.uniform(-10,40)
    rafales = random.uniform(-10,40)
    salaniteEau = random.uniform(0,100)
    densiteeEau = random.uniform(0,100)
    latitude = random.uniform(48.567596,49.286765)
    longitude = random.uniform(-69.059627,-68.739100)
    idShard = 1
    date = 1

    objetDonnee = {"temperatureEau": temperatureEau, "temperatureAir": temperatureAir, "directionVent": directionVent, "kilometrageVent": kilometrageVent, "hauteurMaximum": hauteurMaximum, "vagueMoyenne": vagueMoyenne, "periodeVague": periodeVague, "humidite": humidite, "rafales": rafales, "saliniteEau": salaniteEau, "densiteEau": densiteeEau, "longitude": longitude, "latitude": latitude, "idShard": idShard,"date": date}



    jsonDonnee = json.dumps(objetDonnee)

    #print(temperatureAir,temperatureEau,directionVent,kilometrageVent,hauteurMaximum,vagueMoyenne,periodeVague,humidite,rafales,salaniteEau,densiteeEau)

    donneeDAO.envoyerValeurDirect(jsonDonnee) #envoie les valeurs directement au serveur 

    time.sleep(1)
