# copy image* data folder

#images = ['./data/image1.jpg', './data/image2.jpg', './data/image3.jpg']
images = ['./data/image1.rar', './data/image2.rar', './data/image3.rar']
for image in images:
    print(f"now process file {image}")
    with open(image, 'rb') as file1:
        index = 1
        while (byte := file1.read(1)) != "" and (index := index + 1) < 10:
            x = int.from_bytes(byte, byteorder='little')
            print("%d,%s" % (index, str(hex(x))), end=" ")
        print()