import commands
import json
from items import items
from map import level_blueprint
from os import listdir
from os.path import isfile, join
from terminal_color import color_print


def room_items(room):
    """
    This function creates a list of dictionaries
    Each dictionary contains information about one item
    that exists in this room
    :param room: dict (a dict containing the room information)
    :return: list[dict]
    """
    items_in_room = []
    for item_id in room["items"]:
        for item in items:
            if item_id == item["id"]:
                items_in_room.append(item)
    return items_in_room


def save(row, col, inventory):
    save_name = input("Enter the save file name: ")
    save_name += ".taf"

    save_data = {
        "position": {
            "row": row,
            "col": col
        },
        "inventory": inventory,
        "map": level_blueprint
    }

    with open("./saved_games/" + save_name, "w", encoding="utf-8") as save_file:
        json.dump(save_data, save_file)


def list_of_saved_games():
    files = [file[: -4] for file in listdir("./saved_games") if file.endswith(".taf")]
    return files


def load():
    global level_blueprint
    saved_files = list_of_saved_games()
    print("You have the following save files: ")
    for game in saved_files:
        print(f"\t{game}")

    while True:
        load_name = input("Enter the name of your load file: ")
        if load_name in saved_files:
            break
        color_print("red", f"{load_name} can't be found!")

    load_name += ".taf"

    with open("./saved_games/" + load_name, "r", encoding="utf-8") as load_file:
        load_data = json.load(load_file)

    level_blueprint = load_data["map"]
    inventory = load_data["inventory"]
    row = load_data["position"]["row"]
    col = load_data["position"]["col"]

    return row, col, inventory


def main():
    row = 0
    col = 1
    inventory = []
    running = True

    while running:
        current_location = level_blueprint[row][col]["description"]

        print("You're now", end=' ')
        color_print("green", f"{current_location}")

        items_in_room = room_items(level_blueprint[row][col])

        if len(items_in_room) > 0:
            found_items = [item["name"] for item in items_in_room]
            print("Items in the room:", found_items)

        command = input(">>  ")
        command_parts = command.split()
        main_command = command_parts[0].lower()

        if main_command == "go":
            row, col = commands.movement(command_parts[1].lower(), row, col)
        elif main_command == "get":
            commands.get_item(items_in_room, command_parts[1].lower(), inventory, row, col)
        elif main_command == "drop":
            commands.drop_item(command_parts[1].lower(), inventory, row, col)
        elif main_command == "check":
            if command_parts[1].lower() == "inventory":
                commands.print_inventory(inventory)
            elif command_parts[1].lower() == 'map':
                pass
            elif command_parts[1].lower() == 'commands':
                pass

        elif main_command == "save":
            save(row, col, inventory)

        elif main_command == "load":
            row, col, inventory = load()

        elif main_command == 'quit':
            running = False

        else:
            color_print("red", f"Invalid command!\nI don't understand the command {command_parts[0].upper()}")


if __name__ == "__main__":
    main()
