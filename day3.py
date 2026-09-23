# file=open("text.txt",'w')
# my_file=file.write("This is new file")
# print(my_file)
# file.close()

# file=open('text.txt','r')
# for i in file:
#     print(i)

# file=open("text.txt",'w')
# my_file=file.write("This is new file")
# print(my_file)
# file.close()

# file=open('text.txt','r')
# print(file.read(7))
# file.close()

# file=open('text1.txt','a')
# data=file.write('Hello Rubiccon')
# print(data)
# file.close()    

# # file=open('text1.txt','r')
# # for i in file:
# #     print(i)

# file=open('text1.txt','r')
# my_file=file.read()
# print(my_file)
# file.close()    

# with open('text.txt','r+') as file:
#     file.write('This is new file')
#     print(file.readline())
    
# with open('text.txt','r') as file:
#     data=file.readline()
#     print(data.upper())  

# with open('test.txt','w+') as file:
#      file.write('This is new file')
#      print(file.readline())
    
# with open('test.txt','r') as file:
#      data=file.readline()
#      print(data.upper())  

# import csv
# with open('test.txt','r') as file:
#     myfile=csv.reader(file)
#     x= next(myfile)
#     for row in x:
#         print(row)

# import json
# file = open('local.json','r')
# my_file = file.read()
# a = json.loads(my_file)
# print(a)

# try:
#     A=int(input('Enter 1st number:'))
#     B=int(input('Enter 2nd number:')) 
#     C=A/B
#     print(C)
# except ZeroDivisionError:    
#     print("Can not divide by zero")
# else:
#     print('Division is successful')    

# finally:
#     print('Thanks')    
    
# try:
#      a=int(input('Enter 1st number:'))
#      b=int(input('Enter 2nd number:'))
#      c=a/b
#      print(c)
# except ValueError:
#     print('inside exception')     
    
# try:
#      a = 90
#      b = "k"
#      c = a/b
#      print(c)
# except TypeError:
#     print('inside exception')        
# else:
#     print('inside else')
# finally:
#     print('thanks')    
    
# try:
#     a=int(input('Enter 1st number:'))
#     b=int(input('Enter 2nd number:'))   
#     c=a/b
#     print(c)
# except ArithmeticError:
#     print('Cant be divide by zeero')        
# else:
#     print('Divide by Zero is successful')     
# finally:
#     print('thanks')             


#lambda function
# a= lambda x,y:(x%y)
# print(a(10,20))

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(filter(lambda x: x % 2 == 0, num))
# print(even_num)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_num = list(map(lambda x: x*x , num))
# print(even_num)

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# output = list(filter(lambda x: x % 2 != 0, map(lambda x: x*x, num)))
# print(output)

# def decor_function(function):
#     def product():
#         print('This is very good product')
#         function()  
        
#     return product()
# @decor_function
# def IIT():
#     print('Welcome to IIT Delhi')    

# list=[23,54,63,6,75,45,65,69]
# x=iter(list)
# print(next(x))
# print(next(x))


# def add (a,b):
#     yield a
    
#     yield b
    
# print(add(87,45)) 
# print(type(next))   

# a = 90
# b = 20
# a,b=b,a
# print("a =", a)
# print("b =", b)

# def fun(x,y):
#     z = x,y
#     print(z)
    
# fun(90,10)
# fun(90,'mahto')    

def fun(*x):
    for i in x:
        print(i)
    
fun(90,10)
fun(90,'mahto') 
fun('Kumar','mahto')