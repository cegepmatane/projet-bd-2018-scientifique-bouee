import random
import donneeDAO
import time
import json
from pymongo import MongoClient

running=True

#boucle generant 10 donnees par seconde
while running:
    donnee=[]
    donnee.append(("\"temperature\"",random.uniform(-10,40))) #generation de temperature aleatoire
    donnee.append(("\"salinity\"",random.uniform(0,100))) #generation de salinite aleatoire en %
    donnee.append(("\"difraction\"",random.uniform(0,100))) #generation de difraction aleatoire en %
   
    stringFormatee="{"
    for i in donnee:
        stringFormatee+=str(i[0])
        stringFormatee+=":"
        stringFormatee+="\""+str(i[1])+"\""
        stringFormatee+=","
    
    stringFormatee=stringFormatee[:-1]
    stringFormatee+="}"
    print(stringFormatee)

    donneeDAO.insererValeur(json.loads(stringFormatee)) #envoie les valeurs dans la base mongodb

    time.sleep(0.1)
