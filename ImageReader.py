import extcolors
import numpy as np

#This program opens an image, crops and grayscale it, and then extracts the color from the image
#It will check if the color is greater than the threshold for white to see if health is present
#It will also check if the pixel count for the color is less than 3000(around 40% health)
#If both are true, return true

def getHealthInfo(img):
    i = img.convert("L")
    irotate = i.rotate(-12)
    icrop = irotate.crop((380, 585, 440, 850))
    colors, pixels = extcolors.extract_from_image(icrop, limit = 2)
    for x in colors:
        if all(np.greater_equal(x[0], (200, 200, 200))) and x[1] <= 3000:
            return True
    return False
