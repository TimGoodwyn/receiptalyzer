# Python 2.7
from PIL import Image
from lib.pytesser import pytesser

im = Image.open('lib/pytesser/phototest.tif')
text = pytesser.image_to_string(im)
print text

imagePath = "./data/DSC_2182.JPG"

img = Image.open(imagePath)


# If image is currently landscape, rotate it (hopefully the right way...)
# Assume it's been taken such that the long side of the image is the direction of the receipt
if img.size[0] > img.size[1]:
	img = img.rotate(270)


# Consider transform/deform?
# Consider using ImageMagick for the manipulation?
#img.show()

text2 = pytesser.image_to_string(img)
print text2
