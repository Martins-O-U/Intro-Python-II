from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# setting player's initial location
location_description = Player(room['outside']).location
player_location = Player(room['outside'].name)
player_name = input("Enter Your Adventure name: ")

print(f"Hello {player_name}, Welcome to Treasure Island.")

print(player_location)
print(location_description)

# user choices
user = input(
    " Enter a key: [w] North  [s] South  [d] East  [a] West  [q] Quit\n")

while not user == 'q':
    if user == 'w':
        try:
            location_description = location_description.n_to
            print(location_description)
        except:
            print('choose another direction')
        user = input(
            "Enter a key: [w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 's':
        try:
            location_description = location_description.s_to
            print(location_description)
        except:
            print('choose another direction')
        user = input(
            "Enter a key: [w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 'd':
        try:
            location_description = location_description.e_to
            print(location_description)
        except:
            print('choose another direction')
        user = input(
            "Enter a key: [w] North  [s] South  [d] East  [a] West  [q] Quit\n")
    elif user == 'a':
        try:
            location_description = location_description.e_to
            print(location_description)
        except:
            print('choose another direction')
        user = input(
            "Enter a key: [w] North  [s] South  [d] East  [a] West  [q] Quit\n")
print(f'Game Over!, \n Thanks for playing, {player_name}')
