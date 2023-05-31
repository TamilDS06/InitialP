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
# cv.waitKey(0)

# merging the image
image = cv.merge((blue,green,red)) # it will concatinate 3 channles in to a single image
print(f'shape of the merged image {image.shape}')
# cv.imshow('merged',image)
# cv.waitKey(0)

# Resize the image
image = cv.imread("Rohit_Sharma.png",cv.IMREAD_COLOR)
print(f"The actual size of the image is {image.shape}")
cv.imshow("Resized",image)
image_resized = cv.resize(image, (240,120), interpolation = cv.INTER_NEAREST)
print(f"Resize image shape is {image_resized.shape}")
# cv.imshow("Resized",image_resized)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Rotate the image
image = cv.imread("Rohit_Sharma.png",cv.IMREAD_COLOR)
cv.imshow("Actual",image)
image_rotated = cv.rotate(image, cv.ROTATE_90_COUNTERCLOCKWISE)
# cv.imshow("Rotated",image_rotated)
# cv.waitKey(0)
# cv.destroyAllWindows()

# Rotate the image in a certain angle
img = cv.imread('Rohit_Sharma.png',1)  
# get image height, width
(h, w) = img.shape[:2]
# calculate the center of the image
center = (w / 2, h / 2)
scale = 1.0
# Perform the counter clockwise rotation holding at the center
# 45 degrees
M = cv.getRotationMatrix2D(center, 45, scale)
print(M)
rotated45 = cv.warpAffine(img, M, (h, w))
 
# 110 degrees
M = cv.getRotationMatrix2D(center,110, scale)
rotated110 = cv.warpAffine(img, M, (w, h))
 
# 150 degrees
M = cv.getRotationMatrix2D(center, 150, scale)
rotated150 = cv.warpAffine(img, M, (h, w))
 
 
cv.imshow('Original Image',img)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image
 
cv.imshow('Image rotated by 45 degrees',rotated45)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image
 
cv.imshow('Image rotated by 110 degrees',rotated110)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image
 
cv.imshow('Image rotated by 150 degrees',rotated150)
cv.waitKey(0) # waits until a key is pressed
cv.destroyAllWindows() # destroys the window showing image