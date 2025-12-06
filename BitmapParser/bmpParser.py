#Dictionary to assign every value of "type of conversion" to its meaning
compression = {
    0 : "No compression",
    1 : "RLE 8-bit/pixel",
    2 : "RLE 4-bit/pixel",
    3 : "Huffman 1D",
    4 : "RLE-24",
    5 : "Unknown",
    6 : "RGBA bit field masks",
    11 : "No compression",
    12 : "RLE-8",
    13 : "RLE-4"
}

#Reads until the 18th byte to get the header's dimension and verify if the selected file is a Bitmap file
def read_info_header_version(bmpFile):

    dynamicList = []

    for i in range(0, 18):

        byte = bmpFile.read(1)

        hexadecimal = byte.hex()

        dynamicList.append(hexadecimal)

    if(dynamicList[0] != "42" and dynamicList[1] != "4d"):

        print("This is not a Bitmap file!")

        exit()

    bmpFile.close()

    infoHeaderVersion = int(dynamicList[17] + dynamicList[16] + dynamicList[15] + dynamicList[14], 16)

    if(infoHeaderVersion == 12):
    
        #BITMAPCOREHEADER
        return 0
    
    elif(infoHeaderVersion == 40):

        #BITMAPINFOHEADER
        return 1
    
    
def coreHeader(mainList, bmpFile, infoHeaderVersion):

    for i in range(0, 13):

        byte = bmpFile.read(1)

        hexadecimal = byte.hex()

        mainList.append(hexadecimal)

    print_values(mainList, infoHeaderVersion)


def infoHeaderV1(mainList, bmpFile, infoHeaderVersion):

    for i in range(0, 55):

        byte = bmpFile.read(1)

        hexadecimal = byte.hex()

        mainList.append(hexadecimal)

    print_values(mainList, infoHeaderVersion)       


def print_values(mainList, infoHeaderVersion):

    #VARIABLES DECLARATION

    fileDimension = int(mainList[5] + mainList[4] + mainList[3] + mainList[2], 16)

    offsetBitmapData = int(mainList[13] + mainList[12] + mainList[11] + mainList[10], 16)

    headerLenght = int(mainList[17] + mainList[16] + mainList[15] + mainList[14], 16)

    imageWidth = int(mainList[21] + mainList[20] + mainList[19] + mainList[18], 16)

    imageHeight = int(mainList[25] + mainList[24] + mainList[23] + mainList[22], 16)

    colorDepth = int(mainList[29] + mainList[28], 16)

    compressionType = int(mainList[33] + mainList[32] + mainList[31] + mainList[30], 16)

    imageDimension = int(mainList[37] + mainList[36] + mainList[35] + mainList[34], 16)

    #You can find those informations from BITMAPCOREHEADER and next versions
    if(infoHeaderVersion == 0):

        print("File: Bitmap")

        print(f"File dimension: {fileDimension}B")

        print(f"Offset Bitmap Data: {offsetBitmapData}B")

        print(f"Core header lenght: {headerLenght}B")

        print(f"Image width: {imageWidth}px")

        print(f"Image height: {imageHeight}px")

    #You can find those informations from INFOHEADERV1 and next versions
    elif(infoHeaderVersion == 1):

        print("File: Bitmap")

        print(f"File dimension: {fileDimension}B")

        print(f"Offset Bitmap Data: {offsetBitmapData}B")

        print(f"Info header lenght: {headerLenght}B")

        print(f"Image width: {imageWidth}px")

        print(f"Image height: {imageHeight}px")

        print(f"Color depth: {colorDepth}bit")

        print(f"Compression method: {compression[compressionType]}")

        print(f"Image dimension (Raw): {imageDimension}B")

#START OF THE PROGRAM


#In every list's index there will be 1 byte, represented under hexadecimal format, every byte will be read separately
mainList = []

imagePath = input("Type the image path: ")

file = open(imagePath, "rb")

infoHeaderVersion = read_info_header_version(file)


#I open the file because the old file point was pointing far, but i want to read it from the beginning
file = open(imagePath, "rb")

if(infoHeaderVersion == 0):

    coreHeader(mainList, file, infoHeaderVersion)

else:

    infoHeaderV1(mainList, file, infoHeaderVersion)

file.close()
