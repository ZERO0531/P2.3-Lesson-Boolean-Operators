print("WELCOME TO PETER'S HOUSE!")
print("Would you like to go to the bedroom or to the living room? ")
answer1 = input()
if answer1 == "bedroom": 
    print("You are going to peter's bedroom! See, there is a ardrobe. ")
    print("Would you like to open it? ")
    answer2 = input()
    if answer2 == "yes": 
        print("You are die. ")
    elif answer2 == "no": 
        print("You are still alive. ")
        print("Would you like to go to the living room?")
        answer4 = input()
        if answer4 == "yes": 
            print("You are die")
        else: 
            print("You are clear!")
elif answer1 == "living room": 
    print("You are going to peter's living room! There is a cake! ")
    print("Would you like to eat it? ")
    answer3 = input()
    if answer3 == "yes":
        print("You are die. ")
    elif answer3 == "no": 
        print("You are still alive. ")
        print("Would you like to go to the bedroom?")
        answer5 = input()
        if answer5 == "yes": 
            print("You are going to peter's bedroom! See, there is a ardrobe. ")
            print("Would you like to open it? ")
            answer6 = input()
            if answer6 == "yes": 
                print("You are die. ")
            elif answer6 == "no": 
                print("You are still alive. ")
                print("Would you like to go to the living room?")
                answer7 = input()
                if answer7 == "yes": 
                    print("You are die")
                else: 
                    print("You are clear!")
        if answer5 == "no": 
            print("You are die")
  

