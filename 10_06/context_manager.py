from contextlib import contextmanager


class CFile:
    def __init__(self, file_name, method, encoding="utf-8"):
        self.file = open(file_name, method, encoding=encoding)

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def f_file(file_name, method, encoding="utf-8"):
    file = open(file_name, method, encoding=encoding)
    try:
        yield file
    finally:
        file.close()


def main():
    with CFile("text_file.txt", "w") as out_file:
        out_file.write("Hello there!\n")

    with f_file("text_file.txt", "r") as in_file:
        content = in_file.read()
    print(content)


if __name__ == "__main__":
    main()
