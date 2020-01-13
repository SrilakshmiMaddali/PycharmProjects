import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys(),cutoff=0.8)) >0:
        yn = input("Did you mean  %s instead press Y if yes or N if no: " %get_close_matches(word,data.keys(),cutoff=0.8)[0])
        if yn.upper() == "Y" :
            return data[get_close_matches(word,data.keys(),cutoff=0.8)[0]]
        elif yn.upper() == "N":
            return "Word doesn't exist please check again"
        else:
            return "We didn't understand the entry"
    else:
        return "Word doesn't exist please check again"


myword = input("Enter a word: ")

output = translate(myword)
if isinstance(output,list):
    for item in output:
        print (item)
else :
    print(output)
