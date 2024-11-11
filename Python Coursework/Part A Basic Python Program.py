# Part A: Basic Python Program

print("This is part A of the question")
try: 
    name = input("Enter Your Name: ")
    age = int(input("Enter your age: "))
    BirthYear = 2024 - int(age) # we convert the variable to integer if we do not do it at the previous stage
    print("Hello,", name)
    print("You were born in ", BirthYear)
except ValueError: # This is error handling
    print("You have entered a wrong value") #This displays when the user enters a value that is not an integer for their age
    