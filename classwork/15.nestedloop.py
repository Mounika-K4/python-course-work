for i in range(5):                     #output:#*****
    for j in range(5):                         #*****
        print('*',end="")                      #*****
    print()                                    #*****
                                               #*****
for i in range(5):       #output:00000           
    for j in range(5):          #11111
        print(i,end=" ")        #22222
    print()                     #33333
                                #44444
for i in range(5):             
    for j in range(5):
        print(j,end=" ")   #output:01234
    print()                       #01234
                                  #01234
                                  #01234
                                  #01234

'''
           col 0
    row 0 * * * * *
    print()
           col 1
    row 1 * * * * *
    print()
            col 2
    row 2 * * * * *
    print()
            col 3
    row 3 * * * * *
    print()
            col 4
    row 4 * * * * * 
    print()
    '''