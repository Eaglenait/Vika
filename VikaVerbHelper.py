import json

class VikaVerbHelper:
    def __init__(self):
        path = "/home/seb/vika/verbsWordList.json"
        with open(path, "r") as verbs_file:
            self.verbs_json = json.load(verbs_file)

    #gets the synonyms for a given verb
    def GetVerbSynonyms(self, verb):
        verbIds = list()
        synonyms = list()

        verbIds.extend(verb["s"])
        for verbId in verbIds:
            v = self.FastGetVerbById(verbId)
            synonyms.append(v)
        return synonyms

    #Gets verb as dict by radical
    def GetVerb(self, word):
        for verb in self.verbs_json:
            if verb["r"] in word:
               return verb
        return None

    #Gets verb as dict by Id
    def FastGetVerbById(self, verbId):
        try:
            return self.verbs_json[int(verbId)]
        except IndexError:
            print("FastGetVerbById FastGetVerbById IndexError")

