class Player:
    def __init__(self, position):
        self.position = position
        self.inventory = []

    def go(self, direction: str, exits: list):
        if direction in exits:
            if direction == "north":
                self.position.row -= 1
            elif direction == "south":
                self.position.row += 1
            elif direction == "east":
                self.position.col += 1
            elif direction == "west":
                self.position.col -= 1

    def get_item(self, item: str, room):
        found_item = None
        for i in room.items:
            if i.name == item:
                found_item = i
                break
        if found_item and "get" in found_item.actions:
            room.items.remove(found_item)
            self.inventory.append(found_item)
            print(f"You pick up the {found_item.name}!")
        elif found_item and "get" not in found_item.actions:
            print(f"You can see the {found_item.name}, but you can't pick it up!")
        else:
            print(f"There is no {item} in the room!")

    def drop_item(self, item, room):
        found_item = None
        for i in self.inventory:
            if i.name == item:
                found_item = i
                break
        if found_item and "drop" in found_item.actions:
            self.inventory.remove(found_item)
            room.items.append(found_item)
            print(f"You dropped the {found_item.name}")
        elif found_item and "drop" not in found_item.actions:
            print(f"You have a {found_item.name} in your inventory, but you're not allowed to drop it!")
        else:
            print(f"There is no {item} in your inventory!")

    def check(self, sub):
        if sub == "inventory":
            if len(self.inventory) == 0:
                print("Your inventory is empty")
            else:
                print("You have the following in your inventory: ")
                for item in sorted(self.inventory, key=lambda x: x.name):
                    print(f"* {item.name}")
