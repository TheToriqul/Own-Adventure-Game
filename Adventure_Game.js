const name = prompt("What's your name, brave adventurer?");
console.log("Welcome to the Enigmatic Woods, " + name + "!");

console.log("Sunlight filters through ancient trees, two paths before you. Left to the Whispering Pines, right to the Gurgling Stream. Which calls to you? (left/right)");
const choice = prompt().toLowerCase();

function win(message) {
  console.log(message);
  console.log("Congratulations, " + name + "! You've conquered the Enigmatic Woods!");
}

function lose(message) {
  console.log(message);
  console.log("Better luck next time, " + name + "! Remember, courage and curiosity are key.");
}

if (choice === "left") {
  console.log("Entering the pines, you find a shimmering pool. Drink (drink) or admire (admire)?");
  const action = prompt().toLowerCase();
  if (action === "drink") {
    win("Empowered by the mystical pool, you navigate the woods with newfound confidence.");
  } else if (action === "admire") {
    lose("Lost in the beauty, darkness engulfs you. Remember, adventure demands action!");
  } else {
    lose("Unsure, you wander aimlessly, the woods claiming you in its silence.");
  }

} else if (choice === "right") {
  console.log("Reaching the stream, a rickety bridge sways. Cross (cross) or follow (follow)?");
  const bridge = prompt().toLowerCase();
  if (bridge === "cross") {
    console.log("Halfway across, the bridge groans and gives way! You plunge into the water. Fight (fight) or surrender (surrender)?");
    const swim = prompt().toLowerCase();
    if (swim === "fight") {
      lose("Exhausted from the struggle, you're swept away by the current.");
    } else if (swim === "surrender") {
      win("Carried by the stream, you discover hidden paths and emerge wiser.");
    } else {
      lose("Panic clouds your judgment, leading to a fatal misstep.");
    }
  } else if (bridge === "follow") {
    console.log("A hidden cave behind a waterfall! Enter (enter) or pass (pass)?");
    const cave = prompt().toLowerCase();
    if (cave === "enter") {
      console.log("Inside, a talking raven offers cryptic advice. Heed (heed) or ignore (ignore)?");
      const raven = prompt().toLowerCase();
      if (raven === "heed") {
        // Add additional paths and outcomes based on the raven's advice
        // (Replace this with your creative branching choices!)
        // Example:
        // console.log("The raven croaks, 'Beware the shadows!'");
        // const shadowChoice = prompt("Do you proceed cautiously (cautious) or ignore the warning (ignore)?");
        // // Add further branching logic based on shadowChoice
      } else if (raven === "ignore") {
        lose("Ignoring the wise raven, you remain lost in the woods.");
      } else {
        lose("Confused by the raven's words, you make a wrong turn, never to be seen again.");
      }
    } else if (cave === "pass") {
      lose("Continuing along the stream, you miss the hidden opportunity, forever wondering what lay within.");
    } else {
      lose("Hesitation cripples your progress. The woods reward the bold, not the indecisive.");
    }
  } else {
    lose("Fear clouds your mind, leaving you paralyzed at the crossroads. The woods demand clear choices.");
  }

} else {
  lose("Fear clouds your mind, leaving you paralyzed at the crossroads. The woods demand clear choices.");
}

console.log("Thank you for playing, " + name + "! Come back again and explore the endless possibilities of the Enigmatic Woods!");
