import pickle


def main():
    with open("persons.bin", "rb") as data_file:
        persons = pickle.load(data_file)

    for p in persons:
        print(f"Name: {p['name']}\nAge: {p['age']}\nEmail: {p['email']}\n")


if __name__ == "__main__":
    main()
