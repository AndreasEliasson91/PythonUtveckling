def func(v):
    the_value = v

    def f():
        pass

    def get_v():
        return the_value

    def set_v(v):
        nonlocal the_value
        the_value = v

    f.get_value = get_v
    f.set_value = set_v

    return f


def main():
    obj = func(45)
    print(obj.get_value())
    obj.set_value(33)
    print(obj.get_value())


if __name__ == "__main__":
    main()
