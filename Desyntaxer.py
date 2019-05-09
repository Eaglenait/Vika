import VikaVerbHelper
import VikaObjectHelper
import VikaLocalisationHelper
import VikaSyntax

class Desyntaxer:
    def __init__(self): 
        self.verbHelper = VikaVerbHelper.VikaVerbHelper()
        self.objectHelper = VikaObjectHelper.VikaObjectHelper()
        self.localisationHelper = VikaLocalisationHelper.VikaLocalisationHelper()
        self.syntax = VikaSyntax.VikaSyntax()

    def GetSyntax(self, sentence) -> VikaSyntax:
        print()
        print(sentence)
        for word in sentence.split():
            if(word == "le" or word == 'la'):
                self.syntax.objectPlural = False
                pass
            if( word == 'les'):
                self.syntax.objectPlural = True
                pass

            #verb detection
            currentVerb = self.verbHelper.GetVerb(str(word))
            if currentVerb != None:
                self.syntax.verbs.append(currentVerb)
                syns = self.verbHelper.GetVerbSynonyms(currentVerb)
                for syn in syns:
                    self.syntax.verbs.append(syn)

            #object detection
            currentObject = self.objectHelper.GetObject(str(word))
            if currentObject != None:
                self.syntax.objects.append(currentObject)
                syns = self.objectHelper.GetObjectSynonyms(currentObject)
                for syn in syns:
                    self.syntax.objects.append(syn)

            #localisation detection
            currentLocalisation = self.localisationHelper.GetLocalisation(str(word))
            if currentLocalisation != None:
                self.syntax.localisation.append(currentLocalisation)
                syns = self.localisationHelper.GetLocalisationSynonyms(currentLocalisation)
                for syn in syns:
                    self.syntax.localisation.append(syn)
        return self.syntax
