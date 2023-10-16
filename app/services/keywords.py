import json




def get_keywords():
    with open("equipment.json", "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        a = b = []

        for device in json_data["equipment"]:
            a.append(device["keywords"])
        return a

def get_names():
    a=[]
    with open("equipment.json", "r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)
        for device in json_data["equipment"]:
            a.append(device["name"])
        return a
(get_keywords())