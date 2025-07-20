#conditional statements
#if and else case
items = ['shoes','smartwatch','phone','airpods']
print("Welcome to amazon store..".center(50,"*")) #output:************Welcome to amazon store..*************
searchinput=input("enter:")
if searchinput in items:
    print(f"{searchinput} found.Buy now!!!")      #output:smartwatch found.Buy now!!!
else:
    print(f"{searchinput} is out of stock now.we will notify you")  
                      #output:mobile is out of stock now.we will notify you