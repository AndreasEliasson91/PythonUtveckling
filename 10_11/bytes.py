def main():
    # name = b'Andreas'  # Byte-data per letter, 8-byte value
    name = input("Enter your name: ")
    name = bytes(name, 'utf-8')  # Encoding string, using 'utf-8'

    for c in name:  # ASCII
        print(c)
    print(type(name))


if __name__ == '__main__':
    main()
