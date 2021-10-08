def main():
    # Sum all numbers between 10 and 1,000 (C++ - Style)
    a = 10                      # int a = 10;
    b = 1000                    # int b = 1000;
    total_sum = 0               # int total_sum = 0;

    while b >= a:               # while (b >= a) {
        total_sum += a          #   total_sum += a;
        a += 1                  #   a++;
                                # }
    print(total_sum)            # cout << total_sum << endl;

                                # return 0;

    # Sum all numbers between 10 and 1,000 (Python - Style)
    total_sum = sum(range(10, 1001))
    print(total_sum)


if __name__ == "__main__":
    main()
