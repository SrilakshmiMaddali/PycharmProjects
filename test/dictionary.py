'''
#Convert numbers to word numbers
my_phone_dict={"1":"One","2":"Two","3":"Three","4":"Four","5":"Five","6":"Six","7":"Seven","8":"Eight","9":"Nine","0":"Zero"}
phone=input("Phone:")

output=''
for x in phone:
    output+=my_phone_dict.get(x)
print(output)
'''

#emoji converter

message=input('>')
words=message.split(' ')
emojis={
    ':)':'😀',
    ':(':'☹️'
}
output=''
for word in words:
    output+=emojis.get(word,word)+' '

print(output)
