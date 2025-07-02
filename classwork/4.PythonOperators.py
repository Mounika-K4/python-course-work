#Arthmetic operators
a=10
b=20
print("Addition(+):",a+b)            #Addition(+): 30
print("subtraction(-):",a-b)         #Subtraction(-):-10
print("Multiplication(*):",a*b)      #Multiplication(*): 200
print("division(/):",a/b)            #Division(/):0.5
print("floor division(//):",a//b)    #floor division(//):0
print("Modulus(%):",a%b)             #Modulud(%):10
print("Exponentional(**):",a**b)     #Exponentional(**):1000000000000

#Comparision Operators
a=5                                          
b=10
print("Equal to(==):",a==b)                  #statement:False
print("Not Equal to(!=):",a!=b)              #Statement:True
print("Greater than (>=):",a>b)              #Statement:False
print("less than(<=):",a<b)                  #Statement:True
print("Greater than or Equal to(>=):",a<=b)  #Statement:True
print("less than or equal to(<=):",a<=b)     #Statement:True

#Assignment Operator
a=10
print("Assign(=):",a)                   #Assign(=):10
a=a+5
print("Add & Assign(+=):",a)            #Add & Assign(+=):15
a=a-5
print("subtration & Assign(-=):",a)     #subtration & Assign(-=): 10
a=a*2
print("multiply & Assign(*=):",a)       #multiply & Assign(*=): 20
a=a/5
print("division & Assign(/=):",a)       #division & Assign(/=): 4.0
a=a//1
print("floor division & Assign(//=):",a)   # floor division & Assign(//=): 4.0
a=a**5
print("Exponentional & Assign(**=):",a)    #Exponentional & Assign(**=): 1024.0

#Logical Operator
a=6
b=10
print("And:",a>b and b>a and a<b)         #And: False
print("And:",a%3==0 and b%5==0)           #And: True
print("or:",a%2==0 or b%3==0)             #or: True
print("NOT:",not b%3==0)                  #or: True

#Membership Operations
#list
L=["Mounika","sreeja","harika","bhavana","hema"]
print("mounika" in L)            #Statement:False
print("Mounika" in L)            #Statement:True
print("latha" in L)              #Statement:False
print("bhavana" in L)            #Statement:True
#Tuple
t=(1,2,3,4)
print(1 in t)                  #Statement:True
print(5 in t)                  #Statement:False
print(3 not in t)              #Statement:False
print(4 in t)                  #Statement:True
#Set
s={1,5,8,3}
print(1 in s)                 #Statement:True
print(5 not in s)             #Statement:False
print(4 in s)                 #Statement:False
print(8 in s)                 #Statement:True
#Dictionary
d={'Name':"Mounika",'course':"DS",'age':"21"}
print('Name' in d)                   #Statement:True
print("21" in d)                     #Statement:False
print('course' in d)                 #Statement:True
print('age' in d)                    #Statement:True

#Identitity Operation
a=[1,2,3,4]     
b=[1,2,3,4]
c=[3,4,5,6]
a=b
print(a is b)                    #Statement:True
print(a is not c)                #Statement:True
print(b is c)                    #Statement:False
print(a is c)                    #Statement:False
