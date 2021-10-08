room1 = {
    "description": "in a dark room",
    "items": [],
    "exits": ["south", "east"]
}
room2 = {
    "description": "in a pink room",
    "items": ["id1", "id2", "id3"],
    "exits": ["south", "west"]
}
room3 = {
    "description": "at your starting point",
    "items": [],
    "exits": ["north"]
}
room4 = {
    "description": "in a room with a trap",
    "items": [],
    "exits": ["north", "east"]
}
room5 = {
    "description": "in a dead end",
    "items": ["id4"],
    "exits": ["west"]
}

level_blueprint = [
    [room1, room2],
    [room3, room4, room5]
]
