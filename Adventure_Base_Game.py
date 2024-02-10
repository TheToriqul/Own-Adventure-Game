name = input("Type your name: ")
print("Hello", name + "!", "Welcome to the adventure game.")

answer = input("You are on a dirt road. You can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input("You come to a river. You can walk of swim. Type walk to walk around or swim to swim across: ")

    if answer == "swim":
        print("You swam across and eaten by a Shark. You Lose!")
    elif answer == "walk":
        print("You walked for many miles and you lost the road. So you lost!")
    else:
        print("Not a valid option, you lose.")

elif answer == "right":
    answer = input("You come a wobbly bridge. Do you want cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger man. Do you want to talk them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stranger and they give you gold. YOU WIN!")
        elif answer == "no":
            print("You ignored the stranger and they are offended you. You Lose!")
        else:
            print("Not a valid option. You Lose!")
    else:
        print("Not a valid option. You Lose!")
else:
    print("Not a valid option. You Lose!")

print("Thank you for trying", name)
