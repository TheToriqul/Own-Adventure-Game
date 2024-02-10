package main

import (
	"fmt"
	"strings"
)

func main() {
	name := input("What's your name, brave adventurer? ")
	fmt.Println("Welcome to the Enigmatic Woods, " + name + "!")

	fmt.Println("Sunlight filters through ancient trees, two paths before you. Left to the Whispering Pines, right to the Gurgling Stream. Which calls to you? (left/right)")
	choice := strings.ToLower(input())

	win := func(message string) {
		fmt.Println(message)
		fmt.Println("Congratulations, " + name + "! You've conquered the Enigmatic Woods!")
	}

	lose := func(message string) {
		fmt.Println(message)
		fmt.Println("Better luck next time, " + name + "! Remember, courage and curiosity are key.")
	}

	switch choice {
	case "left":
		fmt.Println("Entering the pines, you find a shimmering pool. Drink (drink) or admire (admire)?")
		action := strings.ToLower(input())
		switch action {
		case "drink":
			win("Empowered by the mystical pool, you navigate the woods with newfound confidence.")
		case "admire":
			lose("Lost in the beauty, darkness engulfs you. Remember, adventure demands action!")
		default:
			lose("Unsure, you wander aimlessly, the woods claiming you in its silence.")
		}
	case "right":
		fmt.Println("Reaching the stream, a rickety bridge sways. Cross (cross) or follow (follow)?")
		bridge := strings.ToLower(input())
		switch bridge {
		case "cross":
			fmt.Println("Halfway across, the bridge groans and gives way! You plunge into the water. Fight (fight) or surrender (surrender)?")
			swim := strings.ToLower(input())
			switch swim {
			case "fight":
				lose("Exhausted from the struggle, you're swept away by the current.")
			case "surrender":
				win("Carried by the stream, you discover hidden paths and emerge wiser.")
			default:
				lose("Panic clouds your judgment, leading to a fatal misstep.")
			}
		case "follow":
			fmt.Println("A hidden cave behind a waterfall! Enter (enter) or pass (pass)?")
			cave := strings.ToLower(input())
			switch cave {
			case "enter":
				fmt.Println("Inside, a talking raven offers cryptic advice. Heed (heed) or ignore (ignore)?")
				raven := strings.ToLower(input())
				switch raven {
				case "heed":
					// Add branching paths and outcomes here based on raven's advice
					// (Replace this with your creative choices!)
				case "ignore":
					lose("Ignoring the wise raven, you remain lost in the woods.")
				default:
					lose("Confused by the raven's words, you make a wrong turn, never to be seen again.")
				}
			case "pass":
				lose("Continuing along the stream, you miss the hidden opportunity, forever wondering what lay within.")
			default:
				lose("Hesitation cripples your progress. The woods reward the bold, not the indecisive.")
			}
		default:
			lose("Panic clouds your judgment, leading to a fatal misstep.")
		}
	default:
		lose("Fear clouds your mind, leaving you paralyzed at the crossroads. The woods demand clear choices.")
	}

	fmt.Println("Thank you for playing, " + name + "! Come back again and explore the endless possibilities of the Enigmatic Woods!")
}

func input(prompt string) string {
	fmt.Println(prompt)
	var input string
	fmt.Scanln(&input)
	return input
}
