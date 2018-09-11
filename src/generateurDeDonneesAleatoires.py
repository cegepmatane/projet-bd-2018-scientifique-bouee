import random
import donneeDAO
import time
import json
from pymongo import MongoClient

running=True

while running:
    data=[]
    data.append(("\"temperature\"",random.uniform(-10,40))) #generate random temperature
    data.append(("\"salinity\"",random.uniform(0,100))) #generate random salinity in %
    data.append(("\"difraction\"",random.uniform(0,100))) #generate random difraction in %
    
    formatedString="{"
    for i in data:
        formatedString+=str(i[0])
        formatedString+=":"
        formatedString+="\""+str(i[1])+"\""
        formatedString+=","
    
    formatedString=formatedString[:-1]
    formatedString+="}"
    print(formatedString)
    donneeDAO.writeValues(json.loads(formatedString))

    time.sleep(2)


