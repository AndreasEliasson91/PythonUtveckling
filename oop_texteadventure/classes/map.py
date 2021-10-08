from classes.room import Room
from data.room_data import rooms


class Map:
    def __init__(self):
        room_objects = [Room(**r) for r in rooms]
        self.map = [
            [room_objects[0], room_objects[1]],
            [room_objects[2], room_objects[3], room_objects[4]]
        ]

    def get_current_room(self, pos) -> list:
        return self.map[pos.row][pos.col]
