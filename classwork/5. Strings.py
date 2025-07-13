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

#3. String Case Conversion Methods
#Uppercase()
name="Mounika"
print(name.upper())   #Output:MOUNIKA
#Lowercase()
name="MOUNI"
print(name.lower())   #Output:mouni

#capitalize()
name="deekshitha"
print(name.capitalize())   #Output:Deekshitha

#title()
name="string methods"
print(name.title())     #Output:string methods

#swapcase()
name="aBcDeFgHiJ"
print(name.swapcase())    #Output:AbCdEfGhIj

#Casefold()
name="B"
print(name.casefold())   #Output:b

#4.Alignment & Formating Method
#center()
name='mounika'
print(name.center(15,'*'))    #Output: ***mounika****
name="mounika"
print(name.center(25,"$"))    #Output: $$$$$$$$$mounika$$$$$$$$$

#ljust()
name="mouli"
print(name.ljust(10,"^"))     #Output: mouli^^^^^

#rjust()
name="sudha"
print(name.rjust(10,"_"))    #Output: _____sudha

#zfill()
a="583"
print(a.zfill(10))      #Output: 0000000583

#5.Search & Find Methods
#find()
name="manohar"
print(name.find("a"))          #Output: 1
print(name.find("h"))          #Output: 4
print(name.find("m"))          #Output: 0

#rfind()
name="abcdabcdabcdabcd"
print(name.rfind("c"))        #Output: 14

#index()
name="python"
print(name.index("h"))        #Output: 3
print(name.index("n"))        #Output: 5

#rindex()
name="abcdabcdabcdabcd"
print(name.rindex("b"))        #Output: 13
print(name.rindex("c"))        #Output: 14

#count()
name="pythoncourse"
print(name.count("o"))        #output: 2
print(name.count("c"))        #output: 1

#6.String Testing Methods
#startswith()
name="21G21A0208"
print(name.startswith("21"))         #Output: True
print(name.startswith("22"))         #Output: False
print(name.startswith("21G21"))      #Output: True
name="ABCDabcd"
print(name.startswith("ABCD"))       #Output: True
print(name.startswith("abcd"))       #Output: False

#endswith()
name="MOUNIKA"
print(name.endswith("MOUNI"))     #Output: False
print(name.endswith("NIKA"))      #Output: True

#isalpha()
name="HELLO"
print(name.isalpha())    #Output: True
name="1234"
print(name.isalpha())    #Output: False

#isalnum()
name="HELLO"
print(name.isalnum())     #Output: True
name="1234"
print(name.isalnum())     #Output: True
name="@1234"
print(name.isalpha())     #Output: False

#islower()
name="MOULI"
print(name.islower())     #Output: False
name="mouli"
print(name.islower())     #Output: True

#isupper()
name="MOULI"
print(name.isupper())     #Output: True
name="mouli"
print(name.isupper())     #Output: False

#isspacee()
name="     "
print(name.isspace())     #Output: True
name=""
print(name.isspace())     #Output: False

#istitle()
name="print hello"
print(name.istitle())    #Output: False
name="Print Hello"
print(name.istitle())    #Output: True

#isidentifier()
name="Python_1"
print(name.isidentifier())   #Output: True
name="@Python"
print(name.isidentifier())   #Output: False


#7.Replace & Modify Methods
#replace()
name="mouni manovar"
print(name.replace("v","h"))   #Output: mouni manohar
name="sudha mouni"
print(name.replace("n","l"))   #Output: sudha mouli

#translate()
name="abcd"
print(name.translate(str.maketrans("a","x")))    #Output: xbcd

#maketrans()
name="python"
print(name.maketrans("th","#$"))       #Output: {116:,35:,104:,36:}

#8.splitting & Joining Methods
#split()
name="x,y,z"
print(name.split(","))            #Output: ['x','y','z']

#rsplit()
name='u,v,x,y,z'
print(name.rsplit(",",1))        #Output:['u,v,x,y', 'z']

#splitlines()
name="mounika\nkaniyampati"
print(name.splitlines())         #Output:['mounika', 'kaniyampati']

#join()
name="kaniyampati mouli"
print(",".join(name))            #Output:k,a,n,i,y,a,m,p,a,t,i, ,m,o,u,l,i

#partition()
name= "python-course"
print(name.partition("-"))        #Output:('python', '-', 'course')

#rpartition()
name="python-course"
print(name.rpartition(","))           #Output:('', '', 'python-course')
print(name.rpartition("-"))           #Output:('python', '-', 'course')

#9.Whitespace & Trimming Methods
#strip()
name= "Bhavana"
print(name.strip())               #Output:Bhavana

#lstrip()
name="----bhavana"
print(name.lstrip("-"))           #Output:bhavana

#rstrip()
name="bhavana----"
print(name.rstrip("-"))          #Output:bhavana

#10.& Decoding Methods
#encode()
name="mouli"
print(name.encode())              #Output:b'mouli'

#decode()
name=b'mouli'
print(name.decode())             #Output:mouli