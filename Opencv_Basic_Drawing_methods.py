### Opencv basic drawing methods ###
import cv2
import numpy as np

# Drawing Circle
img = cv2.imread("Rohit_Sharma.png")
input_image = img
center = (80,80) # center (point) of the circle. It shoud be x-coordinate, y-coordinate
radius = 55
color = (255,0,0)
thickness = 1
cv2.circle(input_image,center, radius, color, thickness)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Drawing rectangle
start_point = (80,80) # Starting point of the rectangle and it is top left of the rectangle
end_point = (160,160) # Ending point of the rectangle and it is bottom right of the rectangle
color = (0,255,0)
thickness = 1
cv2.rectangle(input_image, start_point, end_point, color, thickness) 
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Drawing lines
start_point = (80,80) # It is the starting point of the line
end_point = (160,160) # It is the ending point of the line
color = (0,0,255)
thickness = 1
cv2.line(input_image, start_point, end_point, color, thickness)
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Drawing polylines
array = np.array([[80,80],[40,70],[30,200],[160,160]], np.int32) # represents the coordinates of vertices into an array of shape nx1x2 where n is number of vertices and it should be of type int32.
color = (255,255,255)
is_closed = True
thickess = 1 #  It is a flag that indicates whether the drawn polylines are closed or not.
cv2.polylines(input_image, [array], is_closed, color, thickness)  
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()

# Write text on image
text = "Rohit" # The text which we want to write on the image.
org = (80,80) # It denotes the Bottom-left corner of the text string on the image. So it is used to set the location of text on the image
font = cv2.FONT_HERSHEY_SIMPLEX # the font of text. Here is the list of supported fonts.
fontscale = 1 # The scale of the font by which you can increase or decrease size
color = (255,0,255)
thickness = 6
cv2.putText(input_image, text, org, font, fontscale, color, thickness)
cv2.imshow('image',img)  
cv2.waitKey(0)  
cv2.destroyAllWindows()