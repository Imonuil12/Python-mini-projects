from tkinter.messagebox import YES


print("Welcome to my computer quiz!")

playing = input("Do you wan to play? ")

if playing != "yes":
    quit()
    
print("Okay! Let's play :)")
score=0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score =+ 1 
else: 
    print("Incorrect!")
    
answer = input("Who is the founder of Apple? ")
if answer.lower() == "Steve Jobs":
    print('Correct!')
    score =+ 1    
else: 
    print("Incorrect!")
    
answer = input("Who is the founder of Microsoft? ")
if answer.lower() == "Bill Gates":
    print('Correct!')
    score =+ 1
else: 
    print("Incorrect!")
answer = input("Who is the greatest foorball player of all time? ")
if answer.lower() == "Messi":
    print('Correct!')
    score =+ 1
else: 
    print("Incorrect!")
    
answer = input("Who is my name? ")
if answer.lower == "Imonuil":
    print('Correct!')
    score =+ 1
else: 
    print("Incorrect!")
    
print("You got " + str(score) + " questions correct!")
print("You got " + str(score/4*100) + "%.")
hello


