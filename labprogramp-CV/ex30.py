import cv2
import numpy as np

# Read image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Create kernel
    kernel = np.ones((5, 5), np.uint8)

    # Dilation
    dilation = cv2.dilate(gray, kernel, iterations=1)

    cv2.imshow("Original Image", gray)
    cv2.imshow("Dilation", dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()