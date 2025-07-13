#1. lists
my_list=[1,2,3,4]
print(type(my_list))           #output:<class 'list'>

#2.emptylist[]
my_list=[]
my_list2= list()              #output:<class 'list'>

#list with elements
int=[1,2,3]                             #output:[1, 2, 3]
fruits=["mango","banana","orange"]      #output: ['mango', 'banana', 'orange']
mixed=[10,3.5,"banana",3+2j]            #output:[10, 3.5, 'banana', (3+2j)]
print(int,fruits,mixed)

#List with Nested list
nested_list=[[1,2,3],['a','b','c']]
print(nested_list)                     #output:[[1, 2, 3], ['a', 'b', 'c']]

#list using list() constructor
t_l=list((1,2,3))               #coverting tuple to list
s_l=list("python")
print(s_l)                       #output:['p', 'y', 't', 'h', 'o', 'n']

#3.Assecending Element in a list
#using indexing 
list=("deepika","Raji","mahi")
print(list[0])                          #output:deepika
print(list[1])                          #output:Raji
print(list[2])                          #output:mahi

#Using slicing
num=[10,20,30,40,50]
print(num[1:3])                   #output:[20, 30]
print(num[0:2])                   #output:[10, 20]
print(num[0:])                    #output:[10, 20, 30, 40, 50]
print(num[:4])                    #output:[10, 20, 30, 40]
print(num[:])                     #output:[10, 20, 30, 40, 50]

#4.Modifying lists
#changing elements
num=[1,2,3,4,5]
num[3]=50
print(num)              #output:[1, 2, 3, 50, 5]

#5.Adding Elements
#append()
num=[10,20,30,40,50]
num.append(60)
print(num)                     #output:[10, 20, 30, 40, 50, 60]
num=[10,30,40,50,60]
num.append(20)
print(num)                     #output:[10, 30, 40, 50, 60, 20]

#insert()
num=[20,40,60,80]
num.insert(100,120)
print(num)                     #output:[20, 40, 60, 80, 120]
num=[20,40,60,80,100]
num.insert(500,150)
print(num)                     #output:[20, 40, 60, 80, 100, 150]
num=[20,40,60,80,100]
num.insert(150,500)
print(num)                     #output:[20, 40, 60, 80, 100, 500]

#Extend()
num=[10,30,50]
num.extend([60,70,80])
print(num)                    #output:[10, 30, 50, 60, 70, 80]

#6.Removing elements
#remove()
num=[10,20,30,40,50,60]
num.remove(50)
print(num)                  #output:[10, 20, 30, 40, 60]

#pop()
num=[10,20,30,40,50,60]
num.pop(2)
print(num)                 #output:[10, 20, 40, 50, 60]
num.pop(0)
print(num)                #output:[20, 40, 50, 60]
num=[10,20,30,40,50]
num.pop()
print(num)                #output:[10, 20, 30, 40]

#delete()
num=[10,20,30,40,50,60]
del num[5]
print(num)                #output:[10, 20, 30, 40, 50]

#clear()
num=[10,20,30,40,50,60]
num.clear()
print(num)               #output:[]

#7.List Methods
l=[11,22,33,11,22,55,44,22]
print(l.count(22))                #output:3
print(l.index(22))               #output:1
print(l.index(55))               #output:5

#sort()
l=[11,22,33,11,22,55,44,22]
l.sort()
print(l)                          #output:[11, 11, 22, 22, 22, 33, 44, 55]
l.reverse()
print(l)                          #output:[55, 44, 33, 22, 22, 22, 11, 11]
l.copy()
print(l)                          #output:[55, 44, 33, 22, 22, 22, 11, 11]
l=[11,22,33,11,22,55,44,22]
l.copy()
print(l)                          #output:[11, 22, 33, 11, 22, 55, 44, 22]

m=[20,30,40,50,60]
m.sort()                      #sorting
print(m)                      #output:[20, 30, 40, 50, 60]
print(sorted(m))              #output:[20, 30, 40, 50, 60]
print(len(m))                 #output:5
print(min(m))                 #output:20
print(max(m))                 #output:60
print(sum(m))                 #output:200
print(any(m))                 #output:True,else is present
print(all(m))                 #output:True,else is present



