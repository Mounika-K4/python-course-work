#String
Name="Mounika"
print(type(Name))     #output:<class 'str>

#1.String Operators
#Concatenation(+)
fname='Kaniyampati'
lname='Mounika'
print(fname+lname)       #output: <class 'str'> (KaniyampatiMounika)


#Repetition(*)
name="Mounika"
print("Mounika"*6)        #output : (mounikamounikamounikamounikaMounikaMounika)

#Indexing
text="Harika"
print(text[4])          #output : k
print(text[2])          #output : r
print(text[-4])         #output : r
print(text[-2])         #output : k

#Slicing
name="Bhavana"
print(name[0:4])      #output : Bhav
print(name[:6])       #output : Bhavan
print(name[2:])       #output : avana
print(name[:])        #output : Bhavana

#Membership
name='Mounika'
print('Mouni' in name)        #output : True
print('Mouni' not in name)    #output : False
print('mouni' not in name)    #output : True
print('mounika' in name)      #output : False


#2. String Functions
#len()
name="mounika"
print(len(name))     #output : 7

#max() and min()
name="mouniKA"
print(max("mouniKa"))    #output : u
print(min("mouniKA"))    #output : a

#Sorted()
name="mouni"
print(sorted("mouni"))     #output : ['i','m','n','o','u']

#chr() and ord()
X=('A')
print(ord(X))      #output : 65
X=('a')
print(ord(X))      #output : 97
X=("@")
print(ord(X))      #output : 64

#Chr()
print(chr(97))    #output : a
print(chr(45))    #output : -
print(chr(81))    #output : Q
