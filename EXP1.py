# Import OpenCV library
import cv2

# Read the image
image = cv2.imread(r"C:\Users\gunal\Downloads\tree.jpeg")   # Replace 'image.jpg' with your image file name

# Check if the image is loaded successfully
if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow("Original Image", image)
    cv2.imshow("Grayscale Image", gray_image)

    # Save the grayscale image
    cv2.imwrite("grayscale_image.jpg", gray_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()