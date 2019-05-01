import json

class VikaLocalisationHelper:
    def __init__(self):
        path = "/home/seb/vika/locationWordList.json"
        with open(path, "r") as localisation_file:
            self.localisation_json = json.load(localisation_file)

    '''gets the synonyms for a given localisation (localisation as dict)'''
    def GetLocalisationSynonyms(self, loc):
        localisationIds = list()
        synonyms = list()

        localisationIds.extend(loc["s"])
        for localisationId in localisationIds:
            v = self.FastGetLocalisationById(localisationId)
            synonyms.append(v)
        return synonyms

    '''Gets localisation as dict by name'''
    def GetLocalisation(self, localisationName):
        for loc in self.localisation_json:
            if loc["l"] in localisationName:
               return loc
        return None

    '''Gets localisation as dict by Id'''
    def FastGetLocalisationById(self, localisationId):
        try:
            return self.localisation_json[int(localisationId)]
        except IndexError:
            print("FastGetLocalisationById IndexError")

