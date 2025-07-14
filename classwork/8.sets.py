#1.sets
#Creating a set with elements
my_set={1,2,3,4}
#set with duplicate elements
set={1,2,3,4,4}
print(set)                        #Output:{1, 2, 3, 4}

#2.Operations on set
#membership Testing
set={1,2,3,4}
print(3 in set)                        #Output:True
print(5 not in set)                    #Output:True
print(4 in set)                        #Output:True
print(4 not in set)                    #Output:False

#union() or union(|) method
s1={1,2,3,4}
s2={4,5,6,7}
output=s1|s2
print(output)                     #Output:{1, 2, 3, 4, 5, 6, 7}

#Intersection or &
s1={2,3,4}
s2={4,5,6}
result=(s1&s2)
print(result)                #output:{4}
s1={2,3,4}
s2={5,6,7}
result=(s1&s2)
print(result)               #output:set()

#Difference or "-"
s1={1,2,3}
s2={3,5,6}
result=s1-s2
print(result)            #output:{1,2}

#symmetric Difference or ^
s1={1,2,3,4}
s2={4,5,6,7}
result=s1^s2
print(result)             #output:{1, 2, 3, 5, 6, 7}

#subset (<= or issubset() method)
a1={1,2}
a2={1,2,3}
print(a1 <= a2)                  #output:True 
print(a2 <= a1)                  #output:False

#superset (>= issuperset() mothod)
a1={1,2,3}
a2={1,2}
print(a1 >= a2)             #output:True

#Disjoint sets   (isdisjoint() method)
a1={1,2,3}
a2={4,5,6}
print(a1.isdisjoint(a2))          #output:True

#3.sets methods
b1={1,2,3,4}
b2={5,6,7,8}
#add
b1.add(5)
print(b1)              #output:{1, 2, 3, 4, 5}
#remove
b1.remove(5)
print(b1)            #output:{1, 2, 3, 4}
#Discard
b1.discard(2)
print(b1)          #output:{1, 3, 4}
#pop
b1={1,2,3,4}
b1.pop()
print(b1)          #output:{2, 3, 4}
#clear
b2.clear()
print(b2)          #output:set()
#update
b1={1,2,3,4}
b2={5,6,7,8}
b1.update(b2)
print(b1)          #output:{1, 2, 3, 4, 5, 6, 7, 8}

#Intersection_update
names1= {'mouli','manohar','sudha','mounika'}
names2= {'bhavana','harika','hema','srija'}
names1.intersection_update(names2)
print(names1)                              #output:set()
names1= {'mouli','manohar','sudha','mounika'}
names2= {'bhavana','harika','hema','srija','mouli'}
names1.intersection_update(names2)
print(names1)                              #output:{'mouli'}

#difference_update
names1= {'mouli','manohar','sudha','harika'}
names2= {'bhavana','harika','hema','srija'}
names1.difference_update(names2)
print(names1)                            #output:{'mouli', 'sudha', 'manohar'}

#symmetric_difference_update
names1= {'mouli','manohar','sudha','harika'}
names2= {'bhavana','harika','hema','srija'}
names1.symmetric_difference_update(names2)
print(names1)           #output:{'bhavana', 'sudha', 'mouli', 'manohar', 'srija', 'hema'}

#copy()
fruits={'banana','cherry','mango'}
animals={'lion','tiger','cat'}
food=fruits.copy()
print(food)                  #output:{'cherry', 'banana', 'mango'}

#Functions for set
c1={3,5,7}
#len
print(len(c1))
print(c1)
#max
print(max(c1))
print(c1)
#min
print(min(c1))
print(c1)
#sum
print(sum(c1))
print(c1)
#sorted
c4={'classwork'}
print(sorted(c4))
print(c1)





#Creating a frozenset
frozen = frozenset([1,2,3])
print(frozen)                #output:frozen = frozenset([1,2,3])
#Frozen is immutable
#The following will raise an error
#frozen.add(4)










