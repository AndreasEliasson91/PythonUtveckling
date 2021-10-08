from classes.item import Item
from data.items_data import items


class Room:
    def __init__(self, **room):
        self.__dict__ = room
        room_items = []
        for item_id in self.items:
            for item in items:
                if item["id"] == item_id:
                    room_items.append(Item(**item))

        self.items = room_items
