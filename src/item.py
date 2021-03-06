class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __eq__(self, other):
        return self.name.lower() == other.lower()

    def __str__(self):
        return f"a/an {self.name}"

    def on_take(self):
        print(f"{self.name} was picked up")

    def on_drop(self):
        print(f"{self.name} was dropped")
