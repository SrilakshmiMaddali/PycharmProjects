
#fibonacci series
"""
def fib(num):
    a=0
    b=1
    for x in range(num):
        c=a+b
        a=b
        b=c
        print(c,",")
    return b
n= int(input("Enter n value:"))
fib(n)
"""


def emoji_converter(msg):
    words=msg.split(' ')
    emojis={
        ':)':'😀',
        ':(':'☹️'
    }
    output=''
    for word in words:
        output+=emojis.get(word,word)+' '
    return output


message=input('>')
print(emoji_converter(message))