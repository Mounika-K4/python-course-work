products=['cycle','watch','laptop','mouse','mobile']  
items=input("Enter the items:").split()      #Enter the items:cycle watch laptop mouse mobile
                                
for i in items:
    if i in products:
        print (products.index(i),i)       #output:0 cycle
                                          #1 watch
                                          #2 laptop
                                          #3 mouse
                                          #4 mobile
    else:       
        print (f"{i} is not available")    #Enter the items:bike
                                           #output:bike is not available