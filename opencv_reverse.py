import cv2
import numpy as np
from morse import *
from opencv_functions import *

# Camera location
cameraID = 0

# Window height and width
h, w = 480, 480

# Set up capture
cap = cv2.VideoCapture(cameraID)


# Window with live camera feed
while True:
    ret, frame = cap.read()
    cv2.imshow("Camera Feed", frame)
    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        break
    else:
        pass
