names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here
for name in names:
    usernames.append(name.lower().replace(' ','-'))

print(list(usernames))

#count html tags in the list
tokens = ['<greeting>', 'Hello World!', '</greeting>']

count = 0
for token in tokens:
    if token[0] == '<' and token[-1] == '>':
        count += 1

print(count)

#html tag generator
items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
# the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    html_str += "<li>{}</li>\n".format(item)

html_str += "</ul>"

print(html_str)

# number to find the factorial of
number = 6

# start with our product equal to one
product = 1

# write your for loop here
for index in range(1,number+1):
    product*=index


# print the factorial of number
print(product)


#print first name in lower
fnames=[]
lnames=[]
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
fnames=[name.split()[0].lower() for name in names] # write your list comprehension here
lnames=[name.split()[1].lower() for name in names ]

print(fnames)
print(lnames)