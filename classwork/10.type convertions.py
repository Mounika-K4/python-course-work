#1.Coverting from int
a=10
print(type(a))               #output:<class 'int'>
print(float(a))              #output:10.0
print(type(float(a)))        #output:<class 'float'>
print(str(a))                #output:10
print(type(str(a)))          #output:<class 'str'>
print(bool(a))               #output:True
print(type(bool(a)))         #output:<class 'bool'>
print(complex(a))            #output:(10+0j)
print(type(complex(a)))      #output:<class 'complex'>
# int is a single value ...
#we can not convert single to multiple/iteratable vlaues like list,set,tuple,dict
#print(list(a)) #TypeError: 'int' object is not iterable
#print(type(list(a))) #TypeError: 'int' object is not iterable

#2.Converting from float
b=10.0
print(type(b))               #output:<class 'float'>
print(int(b))                #output:10
print(type(int(b)))          #output:<class 'int'>
print(str(b))                #output:10.0
print(type(str(b)))          #output:<class 'str'>
print(bool(b))               #output:True
print(type(bool(b)))         #output:<class 'bool'>
print(complex(b))            #output:(10+0j)
print(type(complex(b)))              #output:<class 'complex'>
# float is a single value ...
#we can not convert single to multiple/iteratable vlaues like list,set,tuple,dict
#print(list(b)) #TypeError: 'int' object is not iterable
#print(type(list(b))) #TypeError: 'int' object is not iterable

#3.Converting from string
s ='Mounika'
print(type(s))                 #output:<class 'str'>
#if want to convert str in int or float the values should be in numeric 
# ex: for int 1,2,3... for float 1.0,2.0,..
s='1'
print(int(s))                   #output:1
print(type(int(s)))             #output:<class 'int'>
s='2.5'
print(type(s))                  #output:<class 'str'>
print(float(s))                 #output:2.5
print(type(float(s)))           #output:<class 'float'>
s='Mouni'
print(bool(s))                    #output:True
print(type(bool(s)))              #output:<class 'bool'>
s='Mouni'
print(list(s))                    #output:['M', 'o', 'u', 'n', 'i']
print(type(list(s)))              #output:<class 'list'>
s='Mouni'
print(tuple(s))                   #output:('M', 'o', 'u', 'n', 'i')
print(type(tuple(s)))             #output:<class 'tuple'>
s='mouni'
print(set(s))                     #output:{'n', 'm', 'o', 'i', 'u'}
print(type(set(s)))               #output:<class 'set'>
s='mouni'
#print(dict(s))
#print(type(dict(s)))

#4.converting fron list
l=[1,2,3,4]
print(type(l))
#we can not convert multiple/iteratable to single vlaues like int,float,complex
#print(int(a)) #TypeError: 'int' object is not iterable
#print(type(int(a)))                   #TypeError: 'int' object is not iterable 
print(tuple(l))                        #output:(1, 2, 3, 4)
print(type(tuple(l)))                  #output:<class 'tuple'>
print(bool(l))                         #output:True (Non-zero str are True)
print(type(bool(l)))                   #output:<class 'bool'>
print(set(l))                          #output:{1, 2, 3, 4}
print(type(set(l)))                    #output:<class 'set'>
#print(dict(l)) 
#print(type(dict(l)))                  #TypeError: cannot convert dictionary update sequence 
#                                       element #0 to a sequence

#5.Converting from tuple
t=(1,2,3,4)
print(type(t))                          #output:<class 'tuple'>
print(list(t))                          #output:[1, 2, 3, 4]
print(type(list(t)))                    #output:<class 'List'>
print(bool(t))                          #output:True (Non-zero str are True)
print(type(bool(t)))                    #output:<class 'bool'>
print(set(t))                           #output:{1, 2, 3, 4}
print(type(set(t)))                     #output:<class 'set'>
print(str(t))                           #output:(1,2,3,4)
print(type(str(t)))                     #output:<class 'str'>
#print(dict(t)) 
#print(type(dict(t))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#6.Converting from set
n={1,2,3,4}
print(type(n))                       #output:<class 'set'>
print(list(n))                       #output:[1, 2, 3, 4]
print(type(list(n)))                 #output:<class 'List'>
print(tuple(n))                      #output:(1, 2, 3, 4)
print(type(tuple(n)))                #output:<class 'tuple'>
print(str(n))                        #output:{1 ,2,3,4}
print(type(str(n)))                  #output:<class 'str'>
#print(dict(n)) 
#print(type(dict(n))) #TypeError: cannot convert dictionary update sequence element #0 to a sequence

#7.converting from dict
d = {1: 1, 2: 4, 3: 9}
print(type(d))                      #output:<class 'dict'>
print(list(d))                      #output:[1, 2, 3]
print(type(list(d)))                #output:<class 'List'>
print(tuple(d))                     #output:(1, 2, 3)
print(type(tuple(d)))               #output:<class 'tuple'>
print(set(d))                       #output:{1, 2, 3}
print(type(set(d)))                 #output:<class 'set'>
print(bool(d))                      #output:True
print(type(bool(d)))                #output:<class 'bool'>
print(str(d))                       #output:{1: 1, 2: 4, 3: 9}
print(type(str(d)))                 #output:<class 'str'>