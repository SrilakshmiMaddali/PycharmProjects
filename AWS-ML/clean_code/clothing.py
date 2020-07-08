class Clothing:
    def __init__(self,color,style,size,price):
        self.color = color
        self.style = style
        self.size = size
        self.price = price


    def change_price(self,price):
        self.price = price

    def calculate_discount(self,discount):
        return self.price*(1-discount)


class Shirt(Clothing):
    def __init__(self,color,style,size,price,long_or_short):
        Clothing.__init__(color,style,size,price)
        self.long_or_short = long_or_short


    def double_price(self):
        self.price = 2*self.price


class Pants(Clothing):
    def __init__(self,color,style,size,price,waist):
        Clothing.__init__(color,style,size,price)
        self.waist = waist

    def calculate_discount(self, discount):
        return self.price * (1 - discount/2)
