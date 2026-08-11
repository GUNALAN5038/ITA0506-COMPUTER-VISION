import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

# Check if the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Get image dimensions
    (h, w) = img.shape[:2]

    # Find the center of the image
    center = (w // 2, h // 2)

    # Rotate 90 degrees clockwise
    M1 = cv2.getRotationMatrix2D(center, -90, 1.0)
    clockwise = cv2.warpAffine(img, M1, (w, h))

    # Rotate 90 degrees counter-clockwise
    M2 = cv2.getRotationMatrix2D(center, 90, 1.0)
    counter_clockwise = cv2.warpAffine(img, M2, (w, h))

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Clockwise Rotation", clockwise)
    cv2.imshow("Counter Clockwise Rotation", counter_clockwise)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()