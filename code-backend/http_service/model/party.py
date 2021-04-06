import json
from datetime import datetime

from pymongo import DESCENDING

from lib.db import MongoSession

COL = "party"

def _timeParser(time: datetime):
    return time.strftime("%Y/%m/%d %I:%M:%S%p")

def storeData(data):
    doc = {}
    raw = json.loads(data["raw"])
    for key in raw:
        doc[key] = raw[key]
    
    # 2021-04-06 18:01:26.697891
    doc["timestamp"] = datetime.strptime(data["timestamp"], "%Y-%m-%d %H:%M:%S.%f")

    with MongoSession("party") as session:
        col = session.get_collection(COL)
        id_ = col.insert_one(doc)
        return id_

def getLatest(limit):
    with MongoSession("party") as session:
        col = session.get_collection(COL)
        res_raw = list(col.find({}, {"_id": 0}, limit=limit).sort("timestamp", DESCENDING))
        res = dict()
        res["data"] = dict()
        
        keys = [k for k in res_raw[0].keys()]
        keys.remove("timestamp")

        res["timestamp"] = []
        for k in keys: 
            res["data"][k] = []
        
        for raw in res_raw:
            for k in keys:
                res["data"][k].append(raw[k])
            res["timestamp"].append(_timeParser(raw["timestamp"]))

        return res

def getLast():
    with MongoSession("party") as session:
        col = session.get_collection(COL)
        res = list(col.find({}, {"_id": 0}, limit=1).sort("timestamp", DESCENDING))
        res[0]["timestamp"] = _timeParser(res[0]["timestamp"])
        return res