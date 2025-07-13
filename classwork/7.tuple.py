#Tuple
#Empty tuple
empty_tuple=()

#single-element Tuple(note the trailing comma)
single_tuple=(5,)

#multiple-element Tuple
my_tuple=(1,"apple",3.5)

#without parentheses (implicit tuple creation)
implicit_tuple=1,2,3,4
print(empty_tuple,single_tuple,my_tuple)          #output:() (5,) (1, 'apple', 3.5)

#Accessing tuple
t=(10,20,30,40)
print(t[0])                #output:10
print(t[-1])               #output:40


#Slicing
t=(10,20,30,40)
print(t[1:4])                  #output:(20, 30, 40)
print(t[-2:])                  #output:(30, 40)
print(t[:-1])                  #output:(10, 20, 30)
print(t[0:])                   #output:(10, 20, 30, 40)
print(t[:3])                   #output:(10, 20, 30)

#operations on tuples
#repetition
tuple=(1,2)
print(tuple*4)                #output:(1, 2, 1, 2, 1, 2, 1, 2)

#concatination
tuple1=(1,2)
tuple2=(3,4)
print(tuple1+tuple2)           #output:(1, 2, 3, 4)

#membership
tuple=(2,3,4,5,6,7)
print(6 in tuple)            #output:True
print(9 in tuple)            #output:False
print(9 not in tuple)        #output:True
print(6 in tuple)            #output:True

#Tuple Unpacking
tuple= ("banana","cherry","mango")
tuple1,tuple2,tuple3=tuple
print(tuple1,tuple2,tuple3)           #output:banana cherry mango
print(tuple1+tuple2+tuple3)           #output:bananacherrymango

#Tuple Methods
t=(1,2,3,4,5,6)
#length of tuple
print(len(t))                     #output:6
#maximum
print(max(t))                     #output:6
#minimum
print(min(t))                     #output:1
#sum of tuple
print(sum(t))                     #output:21
#nested tuple
t=([1,2,3],(4,5,6),{7,8,9})
print(t)                         #output:([1, 2, 3], (4, 5, 6), {8, 9, 7})



