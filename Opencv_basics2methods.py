#######opencv basic function#######
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