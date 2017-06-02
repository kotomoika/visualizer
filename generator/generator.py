import time
import datetime
from pymongo import MongoClient
from random import randint

import json

with open('config.json') as data_file:
    config = json.load(data_file)

client = MongoClient()
db = client.sensory_data

if __name__ == "__main__":
    startTime = time.time() #.__format__('%m/%d/%Y %H:%M')

    i = 1
    while i == 1:
        curTime = time.time() #.__format__('%m/%d/%Y %H:%M')
        diff = curTime - startTime
        if diff > config["period"]:
            db.data.insert_one({
                "longitude": randint(config["min_longitude"], config["max_longitude"]),
                "latitude": randint(config["min_latitude"], config["max_latitude"]),
                "date_time": datetime.datetime.now().__format__('%m/%d/%Y %H:%M')
            })
            print(diff)
            startTime = curTime

