#####################
"""
while True:
    print("Hello")
    if(2>1):
        pass
    print("Hi")
"""
#####################
"""
d = dict(weather = "clima", earth = "terra", rain = "chuva")
def vocab(myword):
    try:
        return d[myword.lower()]
    except KeyError:
        return "This word doesn't exist"


myword=input("Enter word:")

print(vocab(myword))
"""
#####################
import requests

r=requests.get("http://www.pythonhow.com/data/universe.txt",headers = {'user-agent': 'customUserAgent'})
text=r.text
print(text.count("a"))

#####################
import webbrowser

query=input("Enter a word to search: ")
webbrowser.open("https://google.com/search?q=%s"%query)




