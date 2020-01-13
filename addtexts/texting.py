def sentence_maker(phrase):
    interrogatives = ("how","what","why")
    capitalized = phrase.capitalize()
    if phrase.startswith(interrogatives):
        return "{}? ".format(capitalized)
    else:
        return  "{}. ".format(capitalized)




text = ""
mytext=""
while True:
    text = input("Say something: ")
    if text!="\end":
        mytext += sentence_maker(text)
    else:
        break


print(mytext)