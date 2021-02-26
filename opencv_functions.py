import cv2


def cameracheck(camera):
    # Check if specified camera ID is plugged in
    cap = cv2.VideoCapture(camera)
    if cap is None or not cap.isOpened():
        # No camera found at ID position
        print(f"No camera found at ID: {camera}")
        return False
    else:
        # Camera found
        print(f"Using camera ID {}")
        cap.release()
        return True

def main():
    print("Have you run the correct file?")


if __name__ == "__main__":
    main()