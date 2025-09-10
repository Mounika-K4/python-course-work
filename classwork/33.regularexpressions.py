import re
#re.match() "Checks if the pattern matches only at the start of the string."
result=re.match(r'[a-z]','hello world') 
o=re.match(r"\d",'12hello world')

print(result.group() if result else 'No Match')
print(o.group() if result else 'No Match')


#re.search() "Searches for the first occurrence of the pattern anywhere in the string."
r=re.search(r'[0-9]{2}','ds-da-14-15')
m=re.search(r'[a-z]*[0-9]$','hi234402')
x=re.search(r'h?i','hii')
print(r.group() if result else 'No Match')
print(m.group() if result else 'No Match')
print(x.group() if result else 'No Match')

#re.findall() 'Returns all matches in a list.'