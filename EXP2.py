import cv2

# Read the image
image = cv2.imread(r"C:\Users\gunal\Downloads\house.jpeg")   # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Apply Gaussian Blur
    blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

    # Display the original and blurred images
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Image", blurred_image)

    # Save the blurred image
    cv2.imwrite("blurred_photo.jpeg", blurred_image)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()