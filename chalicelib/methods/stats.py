from chalicelib.models.position import PlayerModel, CondensedModel
from chalicelib.methods.utils import get_dynamo_table
from functools import reduce
from decimal import Decimal

table = get_dynamo_table('Players')

def get_all_stats():
    data = table.scan()['Items']
    data = sorted(data, key=lambda x:x["playerId"])
    return PlayerModel().dump(data, many=True).data


def get_condensed_stats():
    data = [arr for arr in table.scan()['Items'] if arr["averageHue"] != -1]
    data = sorted(data, key=lambda x:x["playerId"])
    for d in data:
        d["time"] = reduce(lambda x,y: x+y, d["timeDiff"], 0)
        d["distance"] = reduce(lambda x,y: x+y, d["distanceTraveled"], 0)
        d["speed"] = reduce(lambda x,y: x+y, d["speed"], 0) / len(d["speed"]) if d["speed"] else 0
        del d["position"]
    return CondensedModel().dump(data, many=True).data


def get_stats_num():
    return {"size": len([arr for arr in table.scan()['Items'] if arr["averageHue"] != -1])}
