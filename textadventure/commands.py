from items import items
from map import level_blueprint
from terminal_color import color_print


def movement(direction: str, y_cord: int, x_cord: int) -> tuple[int, int]:
    if direction in level_blueprint[y_cord][x_cord]["exits"]:
        if direction.lower() == "north":
            y_cord -= 1
        elif direction.lower() == "south":
            y_cord += 1
        elif direction.lower() == "west":
            x_cord -= 1
        else:
            x_cord += 1
    else:
        color_print("red", "You can't go there!")

    return y_cord, x_cord


def get_item(room_items: list, item: str, inventory: list, y_cord: int, x_cord: int):
    item_actions = []
    for room_item in room_items:
        if item == room_item["name"]:
            item_actions = room_item["actions"]

    if len(item_actions) > 0:
        if "get" in item_actions:
            print("You pick up the", end=" ")
            color_print("magenta", f"{item}")
            item_id = [room_item["id"] for room_item in room_items if room_item["name"] == item][0]
            level_blueprint[y_cord][x_cord]["items"].remove(item_id)
            inventory.append(item_id)
        else:
            color_print("red", "You can't pick that up!")


def drop_item(item: str, inventory: list, y_cord: int, x_cord: int):
    item_info = [(inv_item["id"], inv_item["actions"]) for inv_item in items if inv_item["name"] == item]

    if len(item_info) >= 1:
        item_id = item_info[0][0]
        item_actions = item_info[0][1]

        if item_id in inventory:
            if "drop" in item_actions:
                inventory.remove(item_id)
                level_blueprint[y_cord][x_cord]["items"].append(item_id)
                print("You drop the", end=" ")
                color_print("magenta", f"{item}")
            else:
                color_print("red", "You can't drop the", " ")
                color_print("magenta", f"{item}", " ")
        else:
            color_print("red", "There is no", " ")
            color_print("magenta", f"{item}", " ")
            color_print("red", "in your inventory!")
    else:
        color_print("red", "There is no", " ")
        color_print("magenta", f"{item}", " ")
        color_print("red", "in your inventory!")


def print_inventory(inventory: list):
    if len(inventory) == 0:
        color_print("red", "Your inventory is empty!")
    else:
        inventory_items = [inv_item["name"] for item_id in inventory for inv_item in items if item_id == inv_item["id"]]
        print("You have the following in your inventory: ")
        for item in inventory_items:
            print("*", end=' ')
            color_print("magenta", f"{item}")
