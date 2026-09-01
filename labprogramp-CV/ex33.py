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

    # Morphological Gradient
    gradient = cv2.morphologyEx(
        gray,
        cv2.MORPH_GRADIENT,
        kernel
    )

    cv2.imshow("Original Image", gray)
    cv2.imshow("Morphological Gradient", gradient)

    cv2.waitKey(0)
    cv2.destroyAllWindows()