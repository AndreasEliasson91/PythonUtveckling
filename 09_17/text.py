def main():
    name = "Glenn"
    my_file = open("textfile.txt", "w", encoding="utf-8")
    my_file.write(f"Hi {name}!\nHow's your day going?\n")
    my_file.close()

    # Same as above, but with automatic clean up and closing
    with open("textfile_2.txt", "w", encoding="utf-8") as my_file:
        my_file.write(f"This is a second file, {name}.\nGood job!\n")

    with open("textfile_2.txt", "r", encoding="utf-8") as my_file:
        # r = my_file.readline().rstrip()
        # print(r)
        # r = my_file.readline()
        # print(r, end="")
        # my_file.seek(0)   # Manipulates the reference point, which byte to read (which "row" to read, BAD explanation)
        # r = my_file.readline()
        # print(r, end="")

        for r in my_file:
            print(r, end="")

    with open("textfile.txt", "r", encoding="utf-8") as my_file:
        [print(line.rstrip()) for line in my_file.readlines()]

    with open("textfile.txt", "r", encoding="utf-8") as my_file:
        r = my_file.read(100)
        print(r)


if __name__ == "__main__":
    main()
