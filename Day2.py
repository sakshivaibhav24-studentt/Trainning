# class product:
#     def show(self):
#         print(self.name)
#         print(self.price)
        
# class IIT(product):
#     def show(self):
#         print("Welcome to IIT Delhi")
        
# obj=IIT()
# obj.name='mobile'
# obj.price=70000
# obj.show()                

# class product:
#     def show(self):
#         print(self.name)
#         print(self.price)
        
# class IIT(product):

#     def show(self):
#         super().show()
#         print("Welcome to IIT Delhi")
        
# obj=IIT()
# obj.name='mobile'
# obj.price=70000
# obj.show()                

class product:
    def show(self,name=''):
        print('This is very good product')
        
obj=product()
obj.show()
obj.show('Laptop')        