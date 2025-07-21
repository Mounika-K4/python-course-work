bullets=10
while bullets>0:
    if bullets>83:
        print("User dead,Game over")
        break     #if breah executes then else not working
    bullets-=1
    print(f"shoot(),{bullets} are left")
else:
    print ("Game over.You win the game") #if else executes then break not working
                          #shoot(),9 are left
                          #shoot(),8 are left
                          #shoot(),7 are left
                          #shoot(),6 are left
                          #shoot(),5 are left
                          #shoot(),4 are left
                          #shoot(),3 are left
                          #shoot(),2 are left
                          #shoot(),1 are left
                          #shoot(),0 are left
                          #Game over.You win the game