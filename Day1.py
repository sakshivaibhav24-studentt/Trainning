# number=4
# for i in range(2, number):
#     if number % i==0:
#         print('This is not a prime number')
#         break
#     else:
#         print('This is prime number')

# list=[34,53,56,45,23,53,22,78]
# output=list[0::2]
# print(output)

# list=[34,53,56,45,23,53,22,78]
# output=list[0::2]
# print(output[::-1])

# list=[34,53,56,45,23,53,22,78]
# output=list[0::2]
# print(output)

# list1=[1,2,1,3,3,43,2]
# output=list(set(list1))
# print(output)

# set={23,14,14,36,57,33,77,32}
# print(set)
# set.add(34)
# print(set)

# set.pop()
# print(set)

# set.copy()
# print(set)

# set.clear()
# print(set)

tuple=(56,98,77,12,16,32)
# print(tuple)
# tuple.index(12)
# print(tuple)

# tuple.count(23)
# print(tuple)

# dict={'name':'rahul', 'address':'Pune', 'Rollno':'323'}
# print(dict)
# for i in dict.keys():
# for i in dict.values():
# for i in dict.items():
# print(dict['address'])
# dict['address']='London'
# dict['email']='hdjskj@gmail.com'
# print(dict)
# del dict['Rollno']
# print(dict)
# dict = {
#     "detail1": { "Name": "Rahul", "Place": "Pune"},
#     "deatil2": {"Name": "Jay","Place": "USA"}
# }
# for i in dict.keys():
# for i in dict.values():
# for i in dict.items():
    # print(i)
    
# for emp,details in dict.items():
#     print(emp)
    
#     for key in details:
#         print(key)    

# for emp,details in dict.items():
#     print(emp)
    
#     for value in details.values():
#         print(value)    

# del dict['detail1']['Name']
# print(dict['detail1'])

# string="Software"
# print(string[::-1])
# print(string)

# string = "Software test"
# output = max(string.split(),key= len)
# print(output)

# string = "Software test"
# output = min(string.split(),key= len)
# print(output)

# string='software'
# output=sorted(string)
# result=''.join(output)
# print(result)

# string='software test'
# output=sorted(string)
# result=''.join(output)
# print(result)

# string='45484531145678software@#^*&&'
# output=''
# for i in string:
#     if i.isalpha():
#         output=output+i
# print(output)

# string='45484531145678software@#^*&&'
# output=''
# for i in string:
#     if i.isnumeric():
#         output=output+i
# print(output)

# string='45484531145678software@#^*&&'
# output=''
# for i in string:
#     if i.isalpha():
#         output=output+i
# print(output[::-1])

# string='45484531145678software@#^*&&'
# output=0
# for i in string:
#     if i.isalpha():
#         output=output+1
# print(output)

string='45484531145678software@#^*&&'
output=''
for i in string:
    if not i.isalnum():
        output=output+i
print(output)
