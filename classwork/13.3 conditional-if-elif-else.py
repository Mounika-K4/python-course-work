#if and elif and else statements
#weekend budget
amount=int(input("Enter the amount you can spend for weekend:"))
if amount >= 20000:
    print("goa trip..")      #goa trip.. if 20000 or more
elif amount >=15000:
    print("shopping..")      #shopping.. if 15000 or more
elif amount >=10000:
    print("shopping..")      #shopping.. if 10000 or more
elif amount >=5000:
    print("cafe/dining..")   #cafe/dining.. if 5000 or more
elif amount >=2000:
    print("Maintainance:")  #maintainance.. if 2000 or more
elif amount >=500:
    print("Go for movie..")   #go for movie.. if 500 or more
elif amount >=100:
    print("Go for street food..")  #go for street food.. if 100 or more
else :
    print("save the money and sleep..")  #save the money and sleep..