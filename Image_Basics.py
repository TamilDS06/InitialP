"""
Referal link:
https://blog.paperspace.com/the-concept-of-images-in-image-processing/#:~:text=a%20spatial%20plane.-,Properties%20of%20Digital%20Images,%2C%20dimension%2C%20pixel%20and%20channel.
"""

import matplotlib.pyplot as plt
import numpy as np
import cv2

#  creating (9, 9) array of zeros
image = np.zeros((9, 9))

#  attempting to visualize array
plt.imshow(image, cmap='gray')


#  creating a 1-D array (vector) of elements ranging from 0 to 80
image = np.arange(81)
#  reshaping vector into 2-D array
image = image.reshape((9, 9))

#  attempting to visualize array
plt.imshow(image, cmap='gray')

#  creating the array
image = np.zeros((9, 9))
image[1, 2:-2] = 1
image[1:-1, 4] = 1
image[-2, 2:4] = 1

plt.imshow(image)

#  indexing and assigning
image[7, 2:4] = 0

def rotate(image_path, angle):
    """
    This function rotates images at right angles
    in a clockwise manner.
    """
    if angle % 90 != 0:
      print('can only rotate at right angles (90, 180, 270, 360)')
      pass
    else:
      #  reading image
      image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
      
      #  rotating image
      if angle == 90:
        image = np.transpose(image) #  transposing array
        image = image[:, ::-1] #  reversing columns
        plt.imshow(image, cmap='gray')
      elif angle == 180:
        image = image[::-1, :] #  reversing rows
        image = image[:, ::-1] #  reversing columns
        plt.imshow(image, cmap='gray')
      elif angle == 270:
        image = np.transpose(image) #  transposing array
        image = image[::-1, :] #  reversing rows
        plt.imshow(image, cmap='gray')
      else:
        image = image
        plt.imshow(image, cmap='gray')
    pass

#  creating a 9x9 pixel image with 3 channels
image = np.zeros((9,9,3)).astype(np.uint8)

#  switching on pixels outlining the figure j in the red channel (channel 0)
image[1, 2:-2, 0] = 255
image[1:-1, 4, 0] = 255
image[-2, 2:4, 0] = 255

plt.imshow(image)

#  switching on pixels outlining the figure j in the red channel (channel 1)
image[1, 2:-2, 0] = 255
image[1:-1, 4, 0] = 255
image[-2, 2:4, 0] = 255

plt.imshow(image)

#  switching on pixels outlining the figure j in the red channel (channel 2)
image[1, 2:-2, 0] = 255
image[1:-1, 4, 0] = 255
image[-2, 2:4, 0] = 255

plt.imshow(image)

#  creating array
image = np.zeros((9,9,3)).astype(np.uint8)

#  assigning background color in each channel
image[:,:,0] = 128
image[:,:,1] = 0
image[:,:,2] = 32

#  outlining figure j in each channel
image[1, 2:-2, 0] = 0
image[1, 2:-2, 1] = 128
image[1, 2:-2, 2] = 128

image[1:-1, 4, 0] = 0
image[1:-1, 4, 1] = 128
image[1:-1, 4, 2] = 128

image[-2, 2:4, 0] = 0
image[-2, 2:4, 1] = 128
image[-2, 2:4, 2] = 128

plt.imshow(image)

#  computing the average value of pixels across channels
image = image.mean(axis=2)
plt.imshow(image)

import cv2 as cv
# To read an image
image_actual = cv.imread("Rohit_Sharma.png", cv.IMREAD_COLOR)
image_grey = cv.imread("Rohit_Sharma.png", cv.IMREAD_GRAYSCALE)
image_unchanged = cv.imread("Rohit_Sharma.png", cv.IMREAD_UNCHANGED)
cv.imshow("Actual", image_actual)
cv.waitKey(1)
cv.destroyAllWindows()

# To write an image
file_location_to_save = "Rohit_Sharma_grey.png"
status = cv.imwrite(file_location_to_save, image_grey)
print(status)

# To access the pixel value of an image
image = cv.imread("Rohit_Sharma.png")
pixel_value = image[100,100]
print(pixel_value)

#shape and size of an image
shape = image.shape # Height(row), width(collumn), channels(BGR)
size = image.size # Height*width*channel(s) = total number of pixels
print(shape)
print(size)

# splitting an image
image = cv.imread("Rohit_Sharma.png",cv.IMREAD_COLOR)
blue,green,red = cv.split(image) # It will seperate the image into channels
b = image[:,:,0] # channels can be seperated through indexing too.
g = image[:,:,1]
r = image[:,:,2]
print(f'shape of blue {blue.shape}, shape of green {green.shape}, shape of red {red.shape}')
# cv.imshow('blue',blue)
# cv.imshow('green',green)
# cv.imshow('red',red)
# cv.waitKey(100000000)

# merging the image
image = cv.merge((blue,green,red)) # it will concatinate 3 channles in to a single image
print(f'shape of the merged image {image.shape}')
# cv.imshow('merged',image)
# cv.waitKey(100000000)


