def main():
    with open("alice.txt", "r", encoding="utf-8") as in_file:   # Open file
        with open("alice_fixed.txt", "w", encoding="utf-8") as out_file:

            write = False   # Bool to check if write
            for line in in_file:
                if write:
                    if not line.startswith("*** "):     # Write if line not starts
                        out_file.write(line)            # with ("*** ")

                if line.startswith("*** "):     # Reads to the line that starts with ("*** ")
                    if not write:   # If write == False -> True
                        write = True
                    else:
                        break       # Breaks the loop and the writing


if __name__ == "__main__":
    main()
