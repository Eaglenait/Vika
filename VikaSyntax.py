class VikaSyntax:
    def __init__(self):
        self.verbs = list()
        self.localisation = list()
        self.objects = list()
        self.objectPlural = bool

    def HasVerb(self, verb: str) -> bool:
        for v in self.verbs:
            if(v["r"] in verb):
                print("Verb found")
                return True
        return False;

    def HasLocalisation(self, loc: str) -> bool:
        for l in self.localisation:
            print(l)
            print(l["n"])
            if(l["n"] in loc):
                print("Localisation found")
                return True
        return False;

    def HasObject(self, obj: str) -> bool:
        for o in self.objects:
            print(o)
            print(o["n"])
            if(o["n"] in obj):
                print("object found")
                return True
        return False;

    def PrintSyntax(self):
        print("Verbs")
        if len(self.verbs) != 0:
            for verb in self.verbs:
                print(verb)
        else:
            print("   No verbs")

        print("Localisation")
        if len(self.localisation) != 0:
            for loc in self.localisation:
                print(loc)
        else:
            print("   No localisations")

        print("Objects")
        if len(self.objects) != 0:
            for obj in self.objects:
                print(obj)
                print("plural: ", self.objectPlural)
        else:
            print("  No objects")

