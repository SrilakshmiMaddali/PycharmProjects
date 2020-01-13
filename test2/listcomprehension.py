squares = [x**2 for x in range(9) if x % 2 == 0]
print(squares)

odd_squares = [x**2 for x in range(10) if x%2!=0]
print(odd_squares)

squares1 = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
print(squares1)


#####extract first names and print lower case
names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]

first_names = [name.split()[0].lower() for name in names ]# write your list comprehension here
print(first_names)


####print multiples of 3 up to 20
multiples_3 =[3*(i+1) for i in range(20)] # write your list comprehension here
print(multiples_3)


####filter names by scores

scores = {
             "Rick Sanchez": 70,
             "Morty Smith": 35,
             "Summer Smith": 82,
             "Jerry Smith": 23,
             "Beth Smith": 98
          }

passed = [name for name,value in scores.items() if value>65]# write your list comprehension here
print(passed)