log ="July 31 07:30:48 mycomputer bad_process[12345]: Error performing package upgrade"
index = log.index("[")
print(log[index+1:index+6])


import re
log ="July 31 07:30:48 mycomputer bad_process[12345]: Error performing package upgrade"
regex = r"\[(\d+)\]"
result= re.search(regex,log)
print(result[1])


print(re.search(r"aza","plaza"))

print(re.search(r"^x","xenon"))

print(re.search(r"a$","cuba"))

print(re.search(r"$a","antlana"))

print(re.search("p.ng","penguin"))

print(re.search("asa","azad")) # returns none as there is no match

print(re.search(r"[Pp]ython","Python")) # matches python or Python

#####character classes

print(re.search(r"[a-z]way","The end of the highway"))

print(re.search(r"[a-z]way","what a way to go"))

print(re.search(r"cloud[a-zA-Z0-9]","cloudy"))

print(re.search(r"cloud[a-zA-Z0-9]","cloudy9"))

print(re.search(r"Py[a-z]*n","Python Programming"))


####doesnt want them to match ^(circum flex)

print(re.search(r"[^a-zA-Z]","This is a sentence with space."))

print(re.search(r"[^a-zA-Z ]","This is a sentence with space."))

############### matching substrings

print(re.search(r"cat|dog","I like dog"))

print(re.search(r"cat|dog","I like cat"))

print(re.search(r"cat|dog","I like  both dogs and cats")) # searches only first matching expression. to find all use the function findall

######### findall function

print(re.findall(r"cat|dog","I like cats and dogs."))

print(re.findall(r"[a-z]way","The end of the highway"))

print(re.findall(r"[a-z]*way","The end of the highway"))



#####################################################
# find matching punctuation marks

def check_punctuation (text):
  result = re.search(r"[,.':?!]", text)
  return result != None

print(check_punctuation("This is a sentence that ends with a period.")) # True
print(check_punctuation("This is a sentence fragment without a period")) # False
print(check_punctuation("Aren't regular expressions awesome?")) # True
print(check_punctuation("Wow! We're really picking up some steam now!")) # True
print(check_punctuation("End of the line")) # False

#############################################################

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

print(re.search("s.i","Srilakshmi",re.IGNORECASE))

##################################################################

###Repetition Qualifiers .* +?

print(re.search(r"Py.*n","Pygmalion"))

print(re.search(r"Py.*n","Python Programming")) # matches Python Programmin

print(re.search(r"Py[a-z]*n","Python Programming")) # Matches only Python by using character class[a-z]

print(re.search(r"Py[a-z]*n","Pyn"))

print(re.search(r"o+l+","gold"))

print(re.search(r"o+l+","wolly"))

print(re.search(r"o+l+","oily"))

#### the ? means the letters before ? are optional

print(re.search(r"p?each","to each of their own"))

print(re.search(r"p?each","I lkie peach"))


###############################################
"""
Fill in the code to check if the text passed includes a possible U.S. zip code, formatted as follows: exactly 5 digits,
 and sometimes, but not always, followed by a dash with 4 more digits. 
The zip code needs to be preceded by at least one space, and cannot be at the start of the text.
"""

import re
def check_zip_code(text):
  result = re.search(r" [0-9][0-9][0-9][0-9][0-9]", text)
  print(result)
  return result != None

print(check_zip_code("The zip codes for New York are 10001 thru 11104.")) # True
print(check_zip_code("90210 is a TV show")) # False
print(check_zip_code("Their address is: 123 Main Street, Anytown, AZ 85258-0001.")) # True
print(check_zip_code("The Parliament of Canada is at 111 Wellington St, Ottawa, ON K1A0A9.")) # False


################################################
#Escaping characters \

####When we see a pattern that includes a backslash, it could be escaping a special regex character or a special string character

# \w matches letters, numbers, and underscores.
# There's also \d for matching digits,
# \s for matching whitespace characters like space, tab or new line,
# \b for word boundaries and a few others.
"""

\d
Matches any decimal digit; this is equivalent to the class [0-9].

\D
Matches any non-digit character; this is equivalent to the class [^0-9].

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].



"""

print(re.search(r".com","welcome"))

print(re.search(r"\.com","welcome"))

print(re.search(r"\.com","google.com"))

print(re.search(r"\w*","This is an example")) # matches only "This" as there is a space


print(re.search("\w*","This_is_an_exmple")) #matches the whole sentence as underscores are accepted with \w

print(re.search(r"A.*a","Argentina"))

print(re.search(r"A.*a","Azerbaijan"))

#to match only beginning and ending letter we need to use ^ at the beginning and $ at the end so it make sure that begging and ending letters match

print(re.search(r"^A.*a$","Azerbaijan"))

print(re.search(r"^A.*a$","Australia"))
#####################################################################
"""
Fill in the code to check if the text passed has at least 2 groups of alphanumeric characters
 (including letters, numbers, and underscores) separated by one or more whitespace characters.
"""

import re
def check_character_groups(text):
  result = re.search(r"[a-z0-9A-Z]\s[a-z0-9A-Z]", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False


#######################################################################


pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"

print(re.search(pattern,"_this_is_valid_variable_name"))

print(re.search(pattern,"This is n't a valid variable "))

print(re.search(pattern,"my_variable"))

print(re.search(pattern,"9myuser_variable"))

#########################################################################
"""
Fill in the code to check if the text passed looks like a standard sentence, 
meaning that it starts with an uppercase letter, 
followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.
"""


import re
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z ]*[\.\?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True


########################################################################################################
"""
The check_web_address function checks if the text passed qualifies as a top-level web address, 
meaning that it contains alphanumeric characters (which includes letters, numbers, and underscores), 
as well as periods, dashes, and a plus sign, followed by a period and a character-only top-level domain such as ".com", ".info", ".edu", etc. 
Fill in the regular expression to do that, using escape characters, wildcards, repetition qualifiers, 
beginning and end-of-line characters, and character classes.
"""

import re
def check_web_address(text):
  pattern = r"^[a-zA-Z_\.-]*$"
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True


"""
The check_time function checks for the time format of a 12-hour clock, as follows: the hour is between 1 and 12, 
with no leading zero, followed by a colon, then minutes between 00 and 59, 
then an optional space, and then AM or PM, in upper or lower case. Fill in the regular expression to do that. 
How many of the concepts that you just learned can you use here?
"""
import re
def check_time(text):
  pattern = r"^(1[0-2]|0?[1-9]):[0-5][0-9]( AM|PM|am|pm)$"
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

###################################################################
#Capturing Groups
#####Portions of the pattern that are enclosed in parenthesis


result= re.search(r"^(\w*), (\w*)$","Srilakshmi, Maddali")
print(result)
print(result.groups())
print(result[0])
print(result[1])
print(result[2])

def rearrange_name(name):
  result = re.search(r"(\w*), (\w*)",name)
  if result is None:
    return name
  return "{} {}".format(result[2],result[1])

print(rearrange_name("Srilakshmi, Maddali"))
print(rearrange_name("Srilakshmi, Tatavarthi"))
"""
Fix the regular expression used in the rearrange_name function
so that it can match middle names, middle initials, as well as double surnames.
"""
def rearrange_name(name):
  result = re.search(r"^(\w*), ([\w \.]*)$", name)
  if result == None:
    return name
  return "{} {}".format(result[2], result[1])

name=rearrange_name("Kennedy, John F.")
print(name)

#####################################################
#more on repetition qualifiers {}
print(re.search(r"[a-zA-Z]{5}","a ghost"))

print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared"))

print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared"))

print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared")) # \b at the beggining and end gived only the specified number of lettered words

print(re.findall(r"\w{5,10}","I taste strawberries"))

print(re.findall(r"\b\w{5,10}\b","I taste strawberries"))

print(re.findall(r"\b\w{5,}\b","I really like strawberries"))

print(re.search(r"\w{,20}","I really like strawberries"))

print(re.search(r"s\w{,20}","I really like strawberries"))


###############################################################
"""
The long_words function returns all words that are at least 7 characters. 
Fill in the regular expression to complete this function.
"""
import re
def long_words(text):
  pattern = r"\w{7,}"
  result = re.findall(pattern, text)
  return result

print(long_words("I like to drink coffee in the morning.")) # ['morning']
print(long_words("I also have a taste for hot chocolate in the afternoon.")) # ['chocolate', 'afternoon']
print(long_words("I never drink tea late at night.")) # []

################################################################
#Extracting a PID Using regexes in Python

def extract_pid(log_line):
  regex=r"\[(\d+)\]"
  result=re.search(regex,log_line)
  if result is None:
    return ""
  return result[1]

print(extract_pid(log))

print(extract_pid("99 elephants in a [cage]"))

##################################################################
"""
Add to the regular expression used in the extract_pid function, 
to return the uppercase message in parenthesis, after the process id.
"""


import re
def extract_pid(log_line):
    regex = r"\b\[(\d+)\]: ([A-Z]*\b)"
    result = re.search(regex, log_line)

    if result is None:
        return None
    return "{} ({})".format(result[1],result[2])

print(extract_pid("July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing package upgrade")) # 12345 (ERROR)
print(extract_pid("99 elephants in a [cage]")) # None
print(extract_pid("A string that also has numbers [34567] but no uppercase message")) # None
print(extract_pid("July 31 08:08:08 mycomputer new_process[67890]: RUNNING Performing backup")) # 67890 (RUNNING)


########################################################################

#Split method

print(re.split(r"[.?!]","One sentence. Another one? And the last one!")) # splits the sentences when it encounters the specific punctuation in regular expression [.?!]

print(re.split(r"([.?!])","One sentence. Another one? And the last one!")) #([.?!]) matches even the punctuations .?!

#sub method to find and replace it with a specific value

print(re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","Received an email from go_nuts95@my.example.com"))

print(re.sub(r"^([\w .-]), ([\w .-]*)$",r"\2 \1","Maddali, Srilakshmi"))