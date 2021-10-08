import pickle
from os import listdir
from typing import Optional

from Classes.map import Map
from Classes.player import Player
from Classes.player_position import PlayerPosition


class Game:
    def __init__(self):
        self.player = Player(PlayerPosition(1, 0))
        self.map = Map()

    def run(self):
        running = True
        while running:
            self.print_room_info()
            main_command, sub_command = self.get_user_input()
            if main_command == "quit":
                running = False
            else:
                self.process_user_input(main_command, sub_command)

    def print_room_info(self):
        current_room = self.map.get_current_room(self.player.position)
        print(f"You are now in {current_room.description}\nThere are exits to {current_room.exits}")

        if len(current_room.items) > 0:
            found_items = [item.name for item in current_room.items]
            print(f"Found the following items: {found_items}")

    @staticmethod
    def get_user_input() -> tuple[str, Optional[str]]:
        while True:
            command = input(">> ").lower()
            commands = command.split()
            if 0 < len(commands) < 2:
                main = commands[0]
                sub = None
                break
            elif 0 < len(commands) < 3:
                main = commands[0]
                sub = commands[1]
                break
            else:
                print("Invalid input!")
        return main, sub

    def process_user_input(self, main: str, sub: str):
        if main == "go":
            self.player.go(sub, self.map.get_current_room(self.player.position).exits)
        elif main == "get":
            self.player.get_item(sub, self.map.get_current_room(self.player.position))
        elif main == "drop":
            self.player.drop_item(sub, self.map.get_current_room(self.player.position))
        elif main == "check":
            self.player.check(sub)

            #     # commands.print_inventory(inventory)
            # elif command_parts[1].lower() == 'map':
            #     pass
            # elif command_parts[1].lower() == 'commands':
            #     pass
        elif main == "save":
            self.save()
        elif main == "load":
            self.load()

    def save(self):
        file_name = input("What would you like to call this save file? ")
        file_name += ".sav"

        data_to_save = {
            "player": self.player,
            "map": self.map
        }

        with open("./SaveFile/" + file_name, "wb") as save_file:
            pickle.dump(data_to_save, save_file)

    def load(self):
        save_files = self.list_save_files()

        while True:
            print("You have the following save files: ")
            for game in save_files:
                print(f"\t{game}")
            file_name = input("Enter the name of the save file to load: ")
            if file_name in save_files:
                break
            else:
                print(f"Couldn't find {file_name}!")

        file_name += ".sav"


    @staticmethod
    def list_save_files() -> list[str]:
        files = [f.replace(".sav", "") for f in listdir("./SaveFiles") if f.endswith(".sav")]
        return files
