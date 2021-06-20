import re
import json
import math

def reader(path):
    file = open(path, "r")
    entity = json.load(file)
    for i in entity:
        data = entity[str(i)]
        data = data["question"]

        #print(data)
        pumper(data)
    
def pumper(data)
        

reader("./test.json")