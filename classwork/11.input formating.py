#1.1 String Input
name=input("Enter your full name:")
print(name)                  #Enter your full name:Mounika
                             #output:Mounika
#1.2 Integer Input
item=int(input("Enter the number of items:"))    #Enter the number of items:20
print(item)                                      #output:20

#1.3 Float Input 
discount=float(input("Enter the number of discount:"))  #Enter the number of discount:5.5
print(discount)                                         #output:5.5

#1.4 Input as List(Space-Separated)
names=input("Enter employee names(space-separated):").split()   
print(names)                  #Enter employee names(space-separated):mouli nikhil manohar sudha
                              #output:['mouli', 'nikhil', 'manohar', 'sudha']

#1.5 Input as List(comma-separated)
tags=input("Enter tags(comma-separated):").split(',')
print(tags)                   #Enter tags(comma-separated):sale,discount,new
                              #output:['sale', 'discount', 'new']

#1.6 List of Integers
marks=list(map(int,input("Enter marks:").split()))
print(marks)                  #Enter marks:75 80 85 90
                              #output:[75, 80, 85, 90]

#1.7 List of Floats
weights=list(map(float,input("Enter weights:").split()))
print(weights)              #Enter weights:5.5 6.2 6.9 4.5
                            #output:[5.5, 6.2, 6.9, 4.5]

#1.8Tuple Input
dimensions=tuple(map(int,input("Enter length,width,height:").split()))
print(dimensions)          #Enter length,width,height:10 20 30
                           #output:(10, 20, 30)


#1.9 Set Input
selected_ids=set(map(int,input("Enter selected image IDs:").split()))
print(selected_ids)                  #Enter selected image IDs:101 102 103 104
                                     #output:{104, 101, 102, 103}

#1.10 Dictionary Input using eval()
profile=eval(input("Enter user profile as a dictionary:"))
print(profile)         #Enter user profile as a dictionary:{'name':'mouli','age':25,'role':'admin'}   
                       #{'name': 'mouli', 'age': 25, 'role': 'admin'}      

#1.11 Multiple Inputs with Unpacking
Username,password=input("Enter username and password:").split()
print("Username:",Username)     #Enter username and password:user02 mypassword583
print("password:",password)     #output:Username: user02
                                 #password: mypassword583








