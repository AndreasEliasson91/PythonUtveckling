def main():
    # C - Style
                                    # int i;
    arr = [1, 2, 3, 4, 5, 6]        # int arr[] = {1, 2, 3, 4, 5, 6};
    length = len(arr)               # int length = sizeof(arr) / sizeof(arr[0});

    for i in range(0, length):      # for(1 = 0; i < length; i++) {
        if arr[i] % 2 == 0:         #   if(arr[i] % 2 == 0) {
            arr[i] *= 2             #       arr[i] *= 2;
                                    #   }
    print(arr)                      # }

                                    # for(i = 0; i < length; i++) {
                                    #       printf(_Format:"%d\n", arr[i]);
                                    # }
                                    # return 0;

    # Python - Style
    arr = [value * 2 if value % 2 == 0 else value for value in range(1, 7)]
    print(arr)


if __name__ == "__main__":
    main()
