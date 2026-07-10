class mobile:
    def __init__(self,brand,price,):
        self.brand = brand
        self.price = price
        self.__password = 123456
        

    def get_password(self):
        return self.__password
    
    def __str__(self):
        return f"Brand: {self.brand}\nPrice: {self.price}\nPassword: {self.get_password()}"
    

mobile1 = mobile("Samsung","25,000/-")
print(mobile1)

print("")

mobile2 = mobile("OPPO","29,999/-")
print(mobile2)
        