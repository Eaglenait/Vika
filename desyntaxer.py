import json
#aucun accent
#forme radicale du verbe

path = "/home/seb/vika/verbsWordList.json"
with open(path, "r") as verbs_file:
    verbs_json = json.load(verbs_file)

sentence = input()

def isVerb(word) -> bool:
    for verb in verbs_json:
        if word.find(verb["r"]):
            print(verb["id"])
            print(verb["s"])
            return True
        else:
            return False

for word in sentence.split():
    if isVerb(str(word)):
        print("verb found: ", word)
