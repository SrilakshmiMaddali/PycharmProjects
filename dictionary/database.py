import mysql.connector
#from difflib import get_close_matches
con=mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"
)

cursor = con.cursor()
myword=input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary where Expression LIKE '%s' "%myword)    #%(myword+'%') )
print(query)
results=cursor.fetchall()

if results:
    for result in results:
        print(result)
else:
    print("Word not found")