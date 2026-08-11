import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if img is None:
    print("Error: Image not found!")
else:
    # Create a blurred image
    blurred = cv2.GaussianBlur(img, (9, 9), 10.0)

    # Perform unsharp masking
    sharpened = cv2.addWeighted(img, 1.5, blurred, -0.5, 0)

    # Display images
    cv2.imshow("Original Image", img)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Sharpened Image", sharpened)

    cv2.waitKey(0)
    cv2.destroyAllWindows()