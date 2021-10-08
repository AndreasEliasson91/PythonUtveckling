import json


def main():
    with open("persons.json", "r") as json_file:
        data = json.load(json_file)


if __name__ == "__main__":
    main()
