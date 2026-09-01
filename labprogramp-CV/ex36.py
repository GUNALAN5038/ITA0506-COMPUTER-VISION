import cv2
import numpy as np

# Read the watch image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Make a copy
result = img.copy()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Reduce noise
gray = cv2.GaussianBlur(gray, (9, 9), 2)

# Detect circular watch face
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=50,
    param1=100,
    param2=35,
    minRadius=30,
    maxRadius=200
)

if circles is not None:

    circles = np.uint16(np.around(circles))

    # Select the first detected circle
    x, y, r = circles[0][0]

    # Draw circle around watch
    cv2.circle(result, (x, y), r, (0, 255, 0), 3)

    # Display label
    cv2.putText(
        result,
        "WATCH",
        (x - 50, y - r - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2
    )

    print("Watch detected successfully!")

else:
    print("Watch face was not detected.")

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Recognised Watch", result)

cv2.waitKey(0)
cv2.destroyAllWindows()