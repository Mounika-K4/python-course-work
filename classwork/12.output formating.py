#1.1 printing Text
print("Hello,World!")              #output:Hello,World!

#1.2 printing Multiple Items
name="mouni"
age=22
print("name:",name,"age",age)       #output:name: mouni age 22

#1.3 using sep to change the separator
print("2024","20","07",sep="-")        #output:2024-20-07

#1.4 using end to control line endings
print("mouni,",end=" ")              
print("course!")                     #output:mouni, course!
print("mouni\ncourse")               #output:mouni
                                     #course
print("Name:\tmouni")                #output:Name:   mouni

#*output formatting
#1 using commas (Simple print Method)
name="mouni"
age=22
score=91.5
#using commas
print("Name:",name,"age:",age,"score:",score)         #output:Name: mouni age: 22 score: 91.5
#using Modulo Operator(% Formatting)
print("Name: %s | age: %d | score: %.2f" %(name,age,score)) #output:Name: mouni | age: 22 | score: 91.50
#using f-strings
print(f"Name:{name} | age:{age} | score:{score:.2f}")      #output:Name:mouni | age:22 | score:91.50
#using str.format()
print("Name:{} | age:{} | score:{:.1f}".format(name,age,score))#output:Name:mouni | age:22 | score:91.5