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

choices = ["n", "s", "w", "e"]
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

# player = Player("Wanderer", room["outside"])

player_name = input("Enter Your Adventure name: ")

player = Player(f'{player_name}', room['outside'])
location_description = Player(f'{player_name}', room['outside']).current_room


def get_input():
    user_choice = input(
        "Enter a key: [n] North  [s] South  [e] East  [w] West  [i] Inventory [t] Take  [d] Drop [q] Quit\n")
    return user_choice


def room_details(r):
    print("\n===============================================")
    print(f'Current Location:- {r.name}.\n {r.description}')
    if len(r.items) == 0:
        print("No item in the room")
    else:
        print("You look around, and see: ", end="")
        for item in r.items:
            print(item, end=", ")

    print("\n===============================================")


def process_input(r, cmd):
    if len(cmd) == 1:
        val = cmd[0]
        if val == "q":
            print(f"Game Over!, \n Hope to see you again {player_name}!")
            exit()

        elif val == "i":
            if len(player.inventory):
                print("Your items are: ")
                for i in player.inventory:
                    print(i.name)
            else:
                print("You are broke broke")
                return

        elif val == 'n':
            try:
                player.current_room = location_description.n_to
                room_details(player.current_room)
            except:
                print('choose another direction')
        elif val == 's':
            try:
                player.current_room = location_description.s_to
                room_details(player.current_room)
            except:
                print('choose another direction')
        elif val == 'e':
            try:
                player.current_room = location_description.e_to
                room_details(player.current_room)
            except:
                print('choose another direction')
        elif val == 'w':
            try:
                player.current_room = location_description.w_to
                room_details(player.current_room)
            except:
                print('choose another direction')
        else:
            print("Invalid input!. Enter \"h\" for help instructions")
            return


print(f"Hello {player_name}, Welcome to Treasure Island.")
room_details(player.current_room)
while True:
    inp = get_input()
    process_input(player.current_room, inp)
