# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, location):
        self.location = location

    def __repr__(self):
        return f'Your current location is : {self.location}'
