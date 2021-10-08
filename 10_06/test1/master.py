def add(a, b):
    return a + b


def get_third_letter_from_input():
    text = input("Type something")
    return text[2]


def print_third_letter():
    letter = get_third_letter_from_input()
    print(letter)

def main():
    print(add(3, 4))


if __name__ == "__main__":
    main()
