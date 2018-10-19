from pymongo import MongoClient


def insererValeur(json):
    try : 
        conn = MongoClient() #connection a la base mongodb
        print("connecte")

        db = conn.scientifique #selection de la base de donnee
        collection = db.donneeBouee #selection de la collection
        print("recuperation collection")

        #insert json
        result = collection.insert(json) #insertion du json
        print("insertion")

    except:
        print("erreur")
        
        
def recupererValeur():
    try : 
        conn = MongoClient()
        print("connecte")

        db = conn.scientifique #selection de la base de donnee

        collection = db.donneeBouee #selection de la collection

        curseur = collection.find() #recuperation de toutes les donnees de la collection

        resultString="" 
        for enregistrement in curseur :
            resultString+=str(enregistrement) #formatage des donnees
            
        collection.drop() #suppression des donnees en local
            
        return str(resultString)
        
    except Exception as e:
    
        return e
