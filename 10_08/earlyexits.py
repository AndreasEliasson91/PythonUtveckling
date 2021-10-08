def check_value(value):
    if value < 0:
        return False
    if 0 < value < 10:
        return True

    for i in range(10):
        if value == i:
            continue
        else:
            value += i

    return True if value < 100 else False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def is_even(x):
    # Rookie mistake
    result = False
    if x % 2 == 0:
        result = True

    return result


def is_even_2(x):
    return x % 2 == 0


def main():
    print(check_value(19))
    print(is_even(10))
    print(is_even(11))
    print(is_even_2(10))
    print(is_even_2(11))

    # Don't do like this!
    is_even_lambda = lambda value: value % 2 == 0
    is_even_lambda(10)
    is_even_lambda(11)

    # Instead like this
    p1 = Point(10, 15)
    p2 = Point(23, 13)
    p3 = Point(16, 27)
    p4 = Point(8, 97)
    points = [p1, p2, p3, p4]

    points.sort(key=lambda obj: obj.x)

    for point in points:
        print(point.x, point.y)

    value = 10

    value = (lambda x: x + 1)(value)

    print(value)


if __name__ == '__main__':
    main()
