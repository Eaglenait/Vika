import VikaVerbHelper
import VikaObjectHelper
import VikaLocalisationHelper
import VikaSyntax

while(True):
    sentence = input() 

    verbHelper = VikaVerbHelper.VikaVerbHelper()
    objectHelper = VikaObjectHelper.VikaObjectHelper()
    localisationHelper = VikaLocalisationHelper.VikaLocalisationHelper()
    syntax = VikaSyntax.VikaSyntax()

    for word in sentence.split():
        #verb detection
        currentVerb = verbHelper.GetVerb(str(word))
        if currentVerb != None:
            syntax.verbs.append(currentVerb)
            syns = verbHelper.GetVerbSynonyms(currentVerb)
            for syn in syns:
                syntax.verbs.append(syn)


        #object detection
        currentObject = objectHelper.GetObject(str(word))
        if currentObject != None:
            syntax.objects.append(currentObject)
            syns = objectHelper.GetObjectSynonyms(currentObject)
            for syn in syns:
                syntax.objects.append(syn)

        #localisation detection
        currentLocalisation = localisationHelper.GetLocalisation(str(word))
        if currentLocalisation != None:
            syntax.localisation.append(currentLocalisation)
            syns = localisationHelper.GetLocalisationSynonyms(currentLocalisation)
            for syn in syns:
                syntax.localisation.append(syn)

    syntax.Print()
