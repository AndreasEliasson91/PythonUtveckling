import json


def main():
    persons = [
        {
            "name": "Lisa",
            "age": 34,
            "email": "lisa@email.com"
        },
        {
            "name": "John",
            "age": 26,
            "email": "j_man@email.com"
        },
        {
            "name": "Eric",
            "age": 49,
            "email": "eric_@email.com"
        }
    ]

    with open("py_person.json", "w") as json_file:
        json.dump(persons, json_file)


if __name__ == "__main__":
    main()
