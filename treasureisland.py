print("Welcome to treasure island your mission is to find Treasure")
direction = input("Do you want to go to Right or Left?: ").lower()
if direction == "right":
    print("Game Over")
elif direction == "left":
    action = input("Do you want to swim or wait?: ").lower()
    if action == "swim":
        print("Game Over")
    elif action == "wait":
        which_door = input("Which door you want to open? Red or Yellow or Blue: ").lower()
        if which_door == "red":
            print("Game Over")
        elif which_door == "yellow":
            print("You Won!!!!")
        elif which_door == "blue":
            print("Game Over")
