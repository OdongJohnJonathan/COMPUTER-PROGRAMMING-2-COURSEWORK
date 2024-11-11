# Part B: Conditional Execution

print("This is part B of the question")
try:    
    FavNumber = int(input("Enter your favorite number(Between 1 and 20): "))
    if (FavNumber > 20):
        print("Your Favorite number is greater than 20")
        exit() #This exit statement stops the following conditions if the favorite number is greater than 20
    elif FavNumber in [2,4,6,8,10,12,14,16,18,20]:
        print("Your favorite number is an even number")
    else :
        print("Your favorite number is an odd number")

    if (FavNumber > 10):
        print("Your Favorite number is greater than 10")
    elif(FavNumber < 10):
        print("Your favorite number is less than 10")
    elif(FavNumber == 10):
        print("Your Favorite number is equal to ten")
except ValueError:
    print("You have entered a wrong value")
    
print("End of question two")
print(" ")
print(" ")
print(" ")