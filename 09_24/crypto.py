def main():
    line = "Alice was beginning to get very tired of sitting by her sister on the"
    password = "s3cr37"
    encrypted = ""
    for i, c in enumerate(line):
        encrypted += chr(ord(c) ^ ord(password[i % len(password)]))
    print(encrypted)

    clear_text = ""
    for i, c in enumerate(encrypted):
        clear_text += chr(ord(c) ^ ord(password[i % len(password)]))
    print(clear_text)


if __name__ == '__main__':
    main()
