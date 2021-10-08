def main():
    with open("image.gif", "rb") as image_file:
        # image_file.seek(13)     # Move reference point 13 bytes
        # for i in range(256):
        #     r = image_file.read(1)
        #     g = image_file.read(1)
        #     b = image_file.read(1)
        #     print(i, r.hex(), g.hex(), b.hex())
        with open("image_2.gif", "wb") as image_copy:
            data = image_file.read(19)      # Read and copy the first 19 bytes
            image_copy.write(data)

            image_copy.write(bytearray([255, 0, 0]))    # Create a bytearray with new color
            image_file.seek(22, 0)      # Move reference point 22 bytes from start (0) (19 bytes + 3 bytes)

            data = image_file.read()    # Read and copy the rest of the GIF-file
            image_copy.write(data)


if __name__ == "__main__":
    main()
