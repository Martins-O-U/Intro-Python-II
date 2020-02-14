from room import Room

from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("Map", "For proper direction")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("Sword", "For protection")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("Key", "Opens Doors")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("Apples", "For refreshment")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("Basket", "Empty Treasure basket")]),
}


# Link rooms together
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


player_name = input("Enter Your Adventure name: ")
player = Player(f'{player_name}', room['outside'])


Entered_choices = ["n", "s", "e", "w"]


def get_input():
    user_choice = input(
        "Enter a key: [n] North , [s] South,  [e] East,  [w] West,  [i] Inventory \nor [take item_name] To-Take-Item,  [drop item_name] To-Drop-Item or [q] To-Quit\n")
    user_choice = user_choice.split(" ")
    return user_choice


def room_details(room):
    print("\n===============================================")
    print(f'Current Location:- {room.name}.\n {room.description}')
    if len(room.items) == 0:
        print("No item in the room")
    else:
        print("You look around, and see: ", end="")
        for item in room.items:
            print(item, end=", ")
            print("\n what would your next action be ?")

    print("\n===============================================")


def process_input(room, choice):
    if len(choice) == 1:
        val = choice[0]
        if val == "q":
            print(f"Game Over!, \n Hope to see you again {player_name}!")
            exit()

        if val in Entered_choices and room[f"{val}_to"] == None:
            print("Choose another direction")
            return

        if val == "inventory" or val == "i":
            if len(player.inventory):
                print("Your items are: ")
                for i in player.inventory:
                    print(i.name)
            else:
                print("You are broke broke")
            return

        if val not in Entered_choices:
            print("Invalid input!. Enter inputs listed as options")
            return

        player.current_room = room[f"{val}_to"]
        room_details(player.current_room)

    elif len(choice) == 2:
        verb, item = choice
        if(verb == "take" or verb == "get"):
            if(item in player.current_room.items):
                item_index = player.current_room.items.index(item)
                removed_item = player.current_room.items.pop(item_index)
                player.inventory.append(removed_item)
                removed_item.on_take()
            else:
                print("That item is not in the room")

        elif(verb == "drop"):
            if(item in player.inventory):
                item_index = player.inventory.index(item)
                removed_item = player.inventory.pop(item_index)
                player.current_room.items.append(removed_item)
                removed_item.on_drop()
            else:
                print("You dpo not have that item in your inventory")


print(f"Hello {player_name}, Welcome to Treasure Island.")
room_details(player.current_room)
while True:
    inputs = get_input()
    process_input(player.current_room, inputs)
