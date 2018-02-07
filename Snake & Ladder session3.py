#Play Snake & Ladder GAME!
import random
count = 0
while(count<=100):
    roll=input("Press r to roll a dice")
    if (roll== 'r') :
        r= random.randint(1,6)
        count=count+r
    else :
        print (" you have entered incorrect option")
    print (" the value of dice is ",r)
    print ("the value of the present state is",count)
    if (count== 8):
            count= 37
            print ("You have climed up the ladder")
    if (count== 11):
            count= 2
            print ("The snake has bitten you")
    if (count== 13):
            count= 34
            print ("You have climed up the ladder")
    if (count== 25):
            count= 4
            print ("The snake has bitten you")
    if (count== 38):
            count= 9
            print ("The snake has bitten you")
    if (count== 40):
            count= 68
            print ("You have climed up the ladder")
    if (count== 52):
            count= 81
            print ("You have climed up the ladder")
    if (count== 65):
            count= 46
            count ("The snake has bitten you")
    if (count== 76):
            count= 97
            print ("You have climed up the ladder")
    if (count== 89):
            count= 70
            print ("The snake has bitten you")
    if (count== 93):
            count= 64
            print ("The snake has bitten you")
            elif count>100
            count=count-r
            print("You have exceeded the limit TRY AGAIN")
                
    if (count== 100):
            print ("YOU HAVE WON THE GAME!!!!")

    
   
    
    
    
            
    
    
