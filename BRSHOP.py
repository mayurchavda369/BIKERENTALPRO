import self as self


class Bikeshop:
    def __init__(self,stock,):
        self.stock=stock
    def displaybike(self):
        print("total bikes",self.stock)
    def rentforbike(self,qty):
        qty="quantity of bike"
        print("rent for bike",qty)
if qty<=0:
    print("enter the positive value or greater then zero")
elif qty>=self.stock:
    print("enter the value (less then stock)")
else:
    self.stock=self.stock-qty
    print("total prices",qty*100)
    print("total bikes",self.stock)

while True:
    obj=Bikeshop(100)
    uc=int(input('''
    1 display stock
    2 rent a bike
    3 exit
    '''))
if uc==1:
    obj.displaybike()
elif uc==2:
    n=int(input("enter the no :- "))
    obj.rentforbike(n)
else:
    print("exit")




