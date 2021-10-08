def my_bad_range(n):
    values = []
    cnt = 0
    while cnt < n:
        values.append(cnt)
        cnt += 1
    return values


def my_good_range(n):
    cnt = 0
    while cnt < n:
        yield cnt
        cnt += 1


def main():
    for i in my_good_range(10000000000000000000000000000):
        print(i)


if __name__ == "__main__":
    main()
