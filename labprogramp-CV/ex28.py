import cv2
import numpy as np

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Boundary detection convolution kernel
    kernel = np.array([
        [-1, -1, -1],
        [-1,  8, -1],
        [-1, -1, -1]
    ])

    # Apply convolution
    boundary = cv2.filter2D(gray, -1, kernel)

    cv2.imshow("Original Image", img)
    cv2.imshow("Boundary Image", boundary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()