import json

class VikaObjectHelper:
    def __init__(self):
        path = "/home/seb/vika/wordLists/objectsWordList.json"
        with open(path, "r") as objects_file:
            self.objects_json = json.load(objects_file)

    '''gets the synonyms for a given object (object as dict)'''
    def GetObjectSynonyms(self, obj):
        objectIds = list()
        synonyms = list()

        objectIds.extend(obj["s"])
        for objectId in objectIds:
            v = self.FastGetObjectById(objectId)
            synonyms.append(v)
        return synonyms

    '''Gets object as dict by name'''
    def GetObject(self, objectName):
        for obj in self.objects_json:
            if obj["n"] in objectName:
               return obj
        return None

    '''Gets object as dict by Id'''
    def FastGetObjectById(self, objectId):
        try:
            return self.objects_json[int(objectId)]
        except IndexError:
            print("FastGetObjectById IndexError")

