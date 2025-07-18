import cv2
import pyperclip



# pass in an image file, best use a png or jpg file and return a grayscale image
def grayscaleImage(image):
    imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Original', imgGray)
    cv2.waitKey(0)  

    return imgGray

# pass in aan image to copress and cluster it into a smaller version 
def clusteringImage(image, scaleStrength):
    ingResolution = image.shape
    #schale image to were the x is 100 and the y to keep the reolution of the original image
    if ingResolution[1] > 100:
        scale = scaleStrength / ingResolution[1]
        newWidth = int(ingResolution[1] * scale)
        newHeight = int(ingResolution[0] * scale)
        imgResized = cv2.resize(image, (newWidth, newHeight), interpolation=cv2.INTER_AREA)
    cv2.imshow('small image', imgResized)
    cv2.waitKey(0)  

    return imgResized

# pass in a grayscale image and return an ascii art image
def aschiiImage(image):
    ascii_chars = "@%#*+=-:. "
    gray0Vallue, gray0Sym = 0, " "
    gray1Vallue, gray1Sym = 32, ","
    gray2Vallue, gray2Sym = 64, ":"
    gray3Vallue, gray3Sym = 96, "-"
    gray4Vallue, gray4Sym = 128, "="
    gray5Vallue, gray5Sym = 160, "+"
    gray6Vallue, gray6Sym = 192, "#"
    gray7Vallue, gray7Sym = 224, "%"
    gray8Vallue, gray8Sym = 255, "@"

    ascii_image = ""

    height, width = image.shape

    for y in range(height):
        for x in range(width):
            gray = image[y, x]  
            if gray <= gray0Vallue:
                ascii_image += gray0Sym
            elif gray <= gray1Vallue:
                ascii_image += gray1Sym
            elif gray <= gray2Vallue:
                ascii_image += gray2Sym
            elif gray <= gray3Vallue:
                ascii_image += gray3Sym
            elif gray <= gray4Vallue:
                ascii_image += gray4Sym
            elif gray <= gray5Vallue:
                ascii_image += gray5Sym
            elif gray <= gray6Vallue:
                ascii_image += gray6Sym
            elif gray <= gray7Vallue:
                ascii_image += gray7Sym
            elif gray <= gray8Vallue:
                ascii_image += gray8Sym
        ascii_image += "\n"

    print(ascii_image)
    pyperclip.copy(ascii_image)  # Copy the ASCII art to clipboard

    return ascii_image

# pass in a color image and return an ascii art image with color
def AsciiImageColour(image):
    gray0Vallue, gray0Sym = 0, " "
    gray1Vallue, gray1Sym = 32, ","
    gray2Vallue, gray2Sym = 64, ":"
    gray3Vallue, gray3Sym = 96, "-"
    gray4Vallue, gray4Sym = 128, "="
    gray5Vallue, gray5Sym = 160, "+"
    gray6Vallue, gray6Sym = 192, "#"
    gray7Vallue, gray7Sym = 224, "%"
    gray8Vallue, gray8Sym = 255, "@"

    ascii_image = ""

    height, width = image.shape

    for y in range(height):
        for x in range(width):
            Blue, Green, Red = image[y, x]  
            gray = int((Blue + Green + Red) / 3)  # Calculate the average gray value     

            if gray <= gray0Vallue:
                ascii_image += gray0Sym
            elif gray <= gray1Vallue:
                ascii_image += gray1Sym
            elif gray <= gray2Vallue:
                ascii_image += gray2Sym
            elif gray <= gray3Vallue:
                ascii_image += gray3Sym
            elif gray <= gray4Vallue:
                ascii_image += gray4Sym
            elif gray <= gray5Vallue:
                ascii_image += gray5Sym
            elif gray <= gray6Vallue:
                ascii_image += gray6Sym
            elif gray <= gray7Vallue:
                ascii_image += gray7Sym
            elif gray <= gray8Vallue:
                ascii_image += gray8Sym
        ascii_image += "\n"

    print(ascii_image)
    pyperclip.copy(ascii_image)  # Copy the ASCII art to clipboard

    return ascii_image

# pass in an ascii image and save it to a file
def SaveAsciiText(ascii_image, filename):
    with open(filename, 'w') as file:
        file.write(ascii_image)
        file.close()

def SaveAsciiImage(ascii_image, filename):
    if not filename.endswith('.txt'):
        filename += '.txt'

imageName = 'IMG_6549(1)(1)'
image = cv2.imread('IMG_6549(1)(1).png')

image = grayscaleImage(image)
image = clusteringImage(image, 1000)
ascii_image = aschiiImage(image)
SaveAsciiText(ascii_image, imageName + '.txt')

# todo
# 1. add a function to save the ascii image to a file
# 2. add a function to save the ascii image to a file with color
# 3. add a function to save the ascii image to a png file
# 4. add a function to save the ascii image to a png file with color
# 5. add a gui to the program
