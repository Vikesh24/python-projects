"""A python script for Treasure Island game a command line based game"""

# ASCII art
print("")
print("                  __..-----')")
print("        ,.--._ .-'_..--...-'")
print("       '-\"'. _/_ /  ..--''\"\"'-.")
print("       _.--\"\"...:._:(_ ..:\"::. ")
print("    .-' ..::--\"\"_(##)#)\"':. \\ \\)    \\ _|_ /")
print("   /_:-:'/  :__(##)##)    ): )   '-./'   '\\.-'")
print("   \"  / |  :' :/\"\"\\///)  /:.'    --(       )--")
print("     / :( :( :(   (#//)  \"       .-'\\.___./'-.")
print("    / :/|\\ :\\_:\\   \\#//\\            /  |  \\")
print("    |:/ | \"\"--':\\   (#//)              '")
print("    \\/  \\ :|  \\ :\\  (#//)")
print("         \\:\\   '.':. \\#//\\")
print("          ':|    \"--'(#///)")
print("                     (#///)")
print("                     (#///)         ___/\"\"\\")
print("                      \\#///\\           oo##")
print("                      (##///)         `-6 #")
print("                      (##///)          ,'`.")
print("                      (##///)         // `.\\\\")
print("                      (##///)        ||o   \\\\")
print("                       \\##///\\        \\-+--//")
print("                       (###///)       :_|_(/")
print("                       (sjw////)__...--:: :...__")
print("                       (#/::'''        :: :     \"\"--.._")
print("                  __..-'''           __;: :            \"-._")
print("          __..--\"\"                  `---/ ;                '._")
print(" ___..--\"\"                             `-'                    \"-..___")
print("   (_ \"\"---....___                                     __...--\"\" _)")
print("     \"\"\"--...  ___\"\"\"\"\"-----......._______......----\"\"\"     --\"\"\"")
print("                   \"\"\"\"       ---.....   ___....----")
print("")

# Print the welcome greeting to the user
print("Welcome to Treasure Island.Your Mission is to find the treasure.")


# Get the user's choice for direction to continue
direction = input("Choose the direction you want to continue [Left/Right]: ")

if direction == "right":  # Check if the direction is right and end the game
    print("You fell into the hole...Game Over")

elif direction == "left":  # Check if the direction is left and proceed the game accordingly
    print("You have reached the river")

    # Get the users choice for swin or wait to cross the river
    swim_or_wait = input(
        "Do you want to wait for the boat or swin to cross the river? ")

    if swim_or_wait == "swim":  # Check if the user's choice is swin and end the game
        print("Oh Oh...You were attacked by the trout...Game Over")

    elif swim_or_wait == "wait":  # Check if the user's choice is wait and proceed the game
        print("Your Boat has arrived")
        print("Yay you successfully crossed the river to reach the palace")
        print("You have three doors in front of you. red, yellow and blue")

        # Get the user's choice for the door to be opened
        door = input("Choose the door you want to open: ")

        if door == "red":  # Check if the user's choice is red and end the game
            print("Oh oh this room is on fire...Game Over")

        elif door == "blue":  # Check if the user's choice is blue and end the game
            print("Oh Oh you were eaen by beasts...Game Over")

        elif door == "yellow":  # Check if the user's choice is yellow and print the winning message
            print("Yay you reached the treasure...You won the game")

        else:  # Exit the game if user chooses a invalid choice
            print("Incorrect Choice, Game Over")

    else:  # Exit the game if user chooses a invalid choice
        print("Incorrect Choice...Game Over")

else:  # Exit the game if user chooses a invalid choice
    print("Incorrect Choice, Game Over")
