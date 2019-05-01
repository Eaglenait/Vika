import VikaVerbHelper
import VikaSyntax

sentence = input()

verbHelper = VikaVerbHelper.VikaVerbHelper()
syntax = VikaSyntax.VikaSyntax()

for word in sentence.split():
    currentVerb = verbHelper.GetVerb(str(word))
    if currentVerb != None:
        syntax.verbs.append(currentVerb)

syntax.Print()
