<<<<<<< HEAD
name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")
        
elif answer == "right":
    answer = input("You come to a bridge, it looks wobby, do you want to cross it or head back? ")
if answer == "back":
        print("You go back and loose!")
elif answer == "cross":
    answer = input("You cross the bridge and meet a stranger. Do you talk to them?")

    if answer == "yes":
        print("You talk to the stranger and they give you gold. You WIN!")
    elif answer == "no":
        print("You ignore the stranger and they are offended so you loose!")
    else:
        print("Not a valid option. You lose.")


else:
    print("Not a valid option. You lose.")
    
print("Than you for trying", name)
||||||| 4a90e16
=======
name = input('Type your name: ')
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()


if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around and swim to swim across: ")

    if answer == "swim":
        print()
    elif answer == "walk":
        print()
    else:
        print("Not a valid option. You lose.")
elif answer == "right":
    print()
else:
    print("Not a valid option. You lose.")
>>>>>>> 20439d9eabdd05cd4010fe3c6e95ee9a092508c8
