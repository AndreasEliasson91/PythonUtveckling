def main():
    letter = 'A'
    print(ord(letter))      # ord(): Takes an char and convert it to an int (ASCII): chr() is the opposite

    x = 'A'
    y = 's'
    print(x + "\t" + y + "\n=\t=")
    x = ord(x)
    y = ord(y)
    print(x, y)

    z = x ^ y               # z = x XOR y
    print(z, " = ", chr(z))


if __name__ == "__main__":
    main()
