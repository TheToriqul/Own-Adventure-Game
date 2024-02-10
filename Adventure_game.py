name = input("What's your name, brave adventurer? ")
print("Welcome to the Enigmatic Woods, " + name + "!")

print(
    "Sunlight filters through ancient trees, two paths before you. Left to the Whispering Pines, right to the "
    "Gurgling Stream. Which calls to you? (left/right)")
choice = input().lower()


def win(message):
    print(message)
    print("Congratulations, " + name + "! You've conquered the Enigmatic Woods!")


def lose(message):
    print(message)
    print("Better luck next time, " + name + "! Remember, courage and curiosity are key.")


if choice == "left":
    print("Entering the pines, you find a shimmering pool. Drink (drink) or admire (admire)?")
    action = input().lower()
    if action == "drink":
        win("Empowered by the mystical pool, you navigate the woods with newfound confidence.")
    elif action == "admire":
        lose("Lost in the beauty, darkness engulfs you. Remember, adventure demands action!")
    else:
        lose("Unsure, you wander aimlessly, the woods claiming you in its silence.")

elif choice == "right":
    print("Reaching the stream, a rickety bridge sways. Cross (cross) or follow (follow)?")
    bridge = input().lower()
    if bridge == "cross":
        print("Halfway across, the bridge groans and gives way! You plunge into the water. Fight (fight) or surrender "
              "(surrender)?")
        swim = input().lower()
        if swim == "fight":
            lose("Exhausted from the struggle, you're swept away by the current.")
        elif swim == "surrender":
            win("Carried by the stream, you discover hidden paths and emerge wiser.")
        else:
            lose("Panic clouds your judgment, leading to a fatal misstep.")
    elif bridge == "follow":
        print("A hidden cave behind a waterfall! Enter (enter) or pass (pass)?")
        cave = input().lower()
        if cave == "enter":
            print("Inside, a talking raven offers cryptic advice. Heed (heed) or ignore (ignore)?")
            raven = input().lower()
            if raven == "heed":
                pass
            elif raven == "ignore":
                lose("Ignoring the wise raven, you remain lost in the woods.")
            else:
                lose("Confused by the raven's words, you make a wrong turn, never to be seen again.")
        elif cave == "pass":
            lose("Continuing along the stream, you miss the hidden opportunity, forever wondering what lay within.")
        else:
            lose("Hesitation cripples your progress. The woods reward the bold, not the indecisive.")

else:
    lose("Fear clouds your mind, leaving you paralyzed at the crossroads. The woods demand clear choices.")

print("Thank you for playing, " + name + "! Come back again and explore the endless possibilities of the Enigmatic "
                                         "Woods!")
