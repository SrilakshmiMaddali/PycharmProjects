from shirt import Shirt

shirt_one = Shirt('red','S','Full-sleeve',15)
shirt_two = Shirt('Blue','M','Half sleeve',10)

#print(shirt_one.price)
#print(shirt_two.price)

#shirt_two.change_price(20)
#print(shirt_two.price)

#shirt_one.price = 18
#shirt_one.style = 'tank'

shirt_one = Shirt('yellow', 'M', 'long-sleeve', 15)
print(shirt_one.get_price())
shirt_one.set_price(10)