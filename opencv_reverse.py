# Uses camera to detect morse code light flashes and convert to text

from time import time
import cv2
from morse_functions import *
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

# Set up capture
cap = cv2.VideoCapture(cameraID)

# Check camera is plugged in
camera_check(cameraID)

# LED status
previousStatus = False

# Start time
start_time = time()
previousTime = currentTime = 0

# Set a dot time and other required times
dot = float(input("How long for a dot? (seconds)\n"))
word = 7 * dot
letter = 3 * dot

# Reminds user to set box
print("Please select box around morse light source")

# Generate symbol list
symbolList = []
stringWord = ''


# Mouse clicking
def mouse_points(event, x, y, flags, params):
    global LED_x, LED_y, ledClicked
    if event == cv2.EVENT_LBUTTONDBLCLK:
        ledClicked = True
        LED_x = x
        LED_y = y
        print("Button clicked")


# Window with live camera feed
while True:
    ret, frame = cap.read()
    cv2.imshow("Camera Feed", frame)
    cv2.setMouseCallback("Camera Feed", mouse_points)
    if ledClicked:
        break

    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        break
    else:
        pass


while True:
    # Read camera
    ret, frame = cap.read()

    # Get cropping coordinates and crop
    sqc = coordinate_function(LED_x, LED_y, r_size)                                  # Generates coordinates for square
    cv2.rectangle(frame, (sqc[0], sqc[2]), (sqc[1], sqc[3]), r_colour, r_thickness)  # Creates square
    crop = frame[sqc[2]:sqc[3], sqc[0]:sqc[1]]                                       # Crops to square

    # Threshold
    grey = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(grey, 220, 255, cv2.THRESH_BINARY)

    # Show live camera feed and new cropped video
    cv2.imshow("Camera Feed", frame)
    cv2.imshow("LED Area", crop)
    cv2.imshow("grey", grey)
    cv2.imshow("thresh", thresh)

    # Check current LED
    currentStatus = LED_status(thresh)

    # If same as last cycle, pass
    if currentStatus == previousStatus:
        pass

    # If state changed, print current state
    else:
        currentTime = round(time() - start_time, 2)
        diffTime = round(currentTime - previousTime, 2)
        # numTrue = 1
        print(currentStatus, currentTime, diffTime)

        # Determines ends of letters '|' or words '\' when False
        if currentStatus:
            if 0.7 * word < diffTime:
                symbolList.append(stringWord)
                symbolList.append('/')  # Appends / for end of Word
                stringWord = ''
            elif 0.7 * letter < diffTime < 1.3 * letter:
                symbolList.append(stringWord)
                symbolList.append(' ')  # Appends ' ' between letters
                stringWord = ''
        # Adds . or - symbol when True
        else:
            if 2 * dot < diffTime:
                stringWord += '-'
            else:
                stringWord += '.'

    previousStatus = currentStatus
    previousTime = currentTime

    # Wait for escape key
    k = cv2.waitKey(1)
    if k == 27:  # Escape key
        symbolList.append(stringWord)
        print(symbolList)
        print(morse_to_text(symbolList))
        break
    else:
        pass

