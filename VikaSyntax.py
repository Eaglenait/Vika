class VikaSyntax:
    def __init__(self):
        self.verbs = list()
        self.localisation = list()
        
        self.objectPlural = bool
        self.objects = list()

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

