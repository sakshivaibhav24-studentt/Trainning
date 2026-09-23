# class school:
#     def __init__(self):
#         self.__name='DAV'
#         self.__address='Pune'
        
#         print(self.__name)
#         print(self.__address)
# obj=school()        

# class school:
#     def __init__(self):
#         self.name='Delhi Publi School'
#         self.address='mumbai'
        
#         print(self._name)
#         print(self._address)
        
# obj=school()        
        
 
# class mobileinfo():
#     def __init__(self):
#         self._name=''
       
#     def getname(self):
#         return self._name
    
#     def setname(self,name):
#         self._name=name
#         print(self._name)
        
        
# object=mobileinfo()    
# object.getname()
# object.setname('mobile')

# from abc import ABC, abstractmethod
# class product(ABC):
#     @abstractmethod
#     def show(self):
#         pass
    
# class IIT(product):
#     def show(self):
#         print('Welcometo IIT mumbai')
        
# class car(IIT):
#     def show(self):
#         print('This is a car')  
        
# obj=car()
# obj.show()
    
# obj1=IIT()
# obj1.show()  

# class car(IIT):
#     def display(self):
#         print('This is a car')
       
# obj=car()
# obj.show() 
# obj.display()         



string='engineer87665732358'
alpha=''
num=''
for i in string:
    if i.isalpha():
        alpha+=i
    else:
        if i.isnumeric():
         num+=i   
output=''.join(sorted(string))
print(output)
