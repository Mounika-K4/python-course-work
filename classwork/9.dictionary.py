#Dictionary
#1.dictionary example
d_name={"name":"mounika","age":"21","course":"python"}
print(type(d_name))                            #output:<class 'dict'>

#2.Dictionary Operators
#Accessing values
d={"name":"mounika","age":21,"course":"python"}
print(d["name"])                          #Output: mounika
print(d.get("age"))                       #Output: 21

#Differenc Between dict[key] and dict.get(key)
d={"name":"mounika","age":"21","city":"Nellore"}
print(d.get("course", "Not available"))            #Output:Not available

#Adding and Updating Items
d={"name":"mounika","age":21,"city":"Nellore"}
d["course"]="python"
print(d) 
#Output: {'name': 'mounika', 'age': 21, 'city': 'Nellore', 'course': 'python'}

#3.Removing Items from a Dictionary
#Using pop()
details={"name":"mounika","age":21,"branch":"eee","course":"python"}
age=details.pop("age")
print(age)                  #output:21
print(details)
#{'name': 'mounika', 'branch': 'eee', 'course': 'python'} 

#Using del()
del details["course"]
print(details)             #Output: {'name': 'mounika', 'branch': 'eee'}

#Using popitems
details.popitem()
print(details)             #Output: {'name': 'mounika'}

#Using Clear()
details.clear()
print(details)           #Output:{}

#dict.update
d={"name":"mounika","branch":"eee","course":"python"}
d.update({"age":21})
print(d)          #output:{'name': 'mounika', 'branch': 'eee', 'course': 'python', 'age': 21}

#4.Functions for Dictionaries
#len()
d={"name":"mounika","branch":"eee","course":"python"}
print(len(d))              #output:3
#max()
print(max(d))             #output:name
#min()
print(min(d))            #output:branch
#sorted()
print(sorted(d))         #output:['branch', 'course', 'name']

#6.Nested Dictionaries
students={
"mounika":{"age":21,"course":"DS"},
"mouli":{"age":24,"course":"DA"}
}
print(students["mounika"]["course"])     #output:DS
print(students["mouli"]["course"])       #output:DA
