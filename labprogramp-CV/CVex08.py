import cv2

# Read the image
img = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

# Check if the image is loaded
if img is None:
    print("Error: Image not found!")
else:
    # Scale the image to a bigger size (2 times)
    bigger = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

    # Scale the image to a smaller size (0.5 times)
    smaller = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    # Display the images
    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", bigger)
    cv2.imshow("Smaller Image", smaller)

    # Wait for a key press
    cv2.waitKey(0)

    # Close all windows
    cv2.destroyAllWindows()