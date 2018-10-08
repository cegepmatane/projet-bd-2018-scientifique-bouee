from pymongo import MongoClient


def insererValeur(json):
    try : 
        conn = MongoClient()
        print("connected")

        db = conn.scientifique
        collection = db.donneeBouee
        print("get collection")

        #insert json
        result = collection.insert(json) 
        print("inserted ")

    except:
        print("error")
        
        
def recupererValeur():
    try : 
        conn = MongoClient()
        print("connected")

        db = conn.scientifique

        collection = db.donneeBouee

        curseur = collection.find()
        #collection.delete_many()

        resultString="" 
        for enregistrement in curseur :
            resultString+=str(enregistrement)
            
        #curseur.close()
        collection.drop()
            
        return str(resultString)
        
    except Exception as e:
    
        return e
        #return("error")
