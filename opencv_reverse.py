import cv2
import numpy as np
from morse import *
from opencv_functions import *

# Camera location
cameraID = 0

# Click flag
ledClicked = False

# Rectangle size
r_size = 50
r_colour = (0, 128, 0)
r_thickness = 2

# LED Location
LED_x, LED_y = 0, 0
x1, x2, y1, y2 = 0, 0, 0, 0

# Window height and width
h, w = 480, 480

# Set up capture
cap = cv2.VideoCapture(cameraID)

# Check camera is plugged in
cameracheck(cameraID)


# Mouse clicking
def mousepoints(event, x, y, flags, params):
    global LED_x, LED_y, ledClicked, x1, x2, y1, y2
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ledClicked = True
        LED_x = x
        LED_y = y
        print("Button clicked")


# Window with live camera feed
while True:
    ret, frame = cap.read()
    cv2.setMouseCallback("Camera Feed", mousepoints)
    if ledClicked:

        sqc = coordinatefunction(LED_x, LED_y, r_size)
        cv2.rectangle(frame, (sqc[0], sqc[2]), (sqc[1], sqc[3]), r_colour, r_thickness)
        crop = frame[sqc[2]:sqc[3], sqc[0]:sqc[1]]
        cv2.imshow("test crop", crop)

    cv2.imshow("Camera Feed", frame)

    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        break
    else:
        pass
