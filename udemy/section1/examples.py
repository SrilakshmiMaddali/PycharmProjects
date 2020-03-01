def bmicalculator(weight,height):
    result=weight/(height**2)
    return (result)


print(bmicalculator(68,100))


def add_ten(x):
    return(x+10)

def twice(func,arg):
    return func(func(arg))


print(twice(add_ten,10))
################discount on top of student discount
def student_discount(price):
    result=price-(price*10)/100
    return result

def additional_discount(newprice):
    result=newprice-(newprice*5)/100
    return result

print(additional_discount(student_discount(100)))


##################Calculate the value of mathematical expression x*(x+5)^2 where x= 5 using lambda expression.

print((lambda x:x*(x+5)**2)(5))


"""
Consider a list in Python which includes prices of all the items in a store.

Build a function to discount the price of all the products by 10%.

Use map to apply the function to all the elements of the list so that all the product prices are discounted.


"""

price_list = [10,20,30,40,50]
def add_discount(price):
    return price-(price*10)/100

print(list(map(add_discount,price_list)))


#################factorial of x


def factorial(x):
    if x<=0:
        return 1
    return x*factorial(x-1)

print(factorial(5))
