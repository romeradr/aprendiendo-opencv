import cv2 as cv
import numpy as np
import sys

# Imprimo la versión de OpenCV
print(cv.__version__)

# Getting started with Images
img = cv.imread(cv.samples.findFile("./samples/starry_night.jpg"))

if img is None:
    sys.exist("Could not read the image.")

# Show the image
cv.imshow("Display window", img)
k = cv.waitKey(0)

# If the user presses the 's' key, save the image in the current directory with the name starry_night.jpg
if k == ord("s"):
    cv.imwrite("starry_night.jpg", img)


# Drawing lines
# Create a black image 
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
cv.line(img, (0, 0), (511, 511), (255, 0, 0), 5)

# Draw a rectangle
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw a circle
cv.circle(img,(447,63), 63, (0,0,255), -1)

# Draw an Ellipse
cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw a polygon
pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
pts = pts.reshape((-1,1,2))
cv.polylines(img,[pts],True,(0,255,255))

# Adding text to image
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500), font, 4,(255,255,255),2,cv.LINE_AA)

# Mostramos la imagen, igual que hemos hecho antes
cv.imshow("Display image", img)
k = cv.waitKey(0)