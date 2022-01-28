import json

class Mission():
    
    def createMission(newEntry):
        jsonFile = open("newMission.json", "w")
        json.dump(newEntry, jsonFile)
        jsonFile.close()