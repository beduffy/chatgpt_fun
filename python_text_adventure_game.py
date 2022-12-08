# define game location
location = "forest"

# define game inventory
inventory = []

# game loop
while True:
    # display current location and inventory
    print(f"You are in the {location}.")
    print("In your inventory:")
    for item in inventory:
        print(f"- {item}")
    print()

    # get player input
    action = input("What would you like to do? ")

    # handle player actions
    if action == "look":
        # describe current location
        if location == "forest":
            print("You are in a dense forest, with trees all around you. You see a path leading north.")
        elif location == "cave":
            print("You are in a dark cave. You see a flickering light to the east.")
    elif action == "go north":
        # move player to different location
        if location == "forest":
            location = "cave"
        else:
            print("You cannot go in that direction.")
    elif action == "take torch":
        # add item to inventory
        if location == "cave":
            inventory.append("torch")
            print("You take the torch.")
        else:
            print("There is no torch to take.")
    elif action == "quit":
        # end game
        print("Goodbye!")
        break
    else:
        # handle unknown actions
        print("I don't understand what you want to do.")
