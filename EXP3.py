import cv2

# Read the image
image = cv2.imread(r"C:\Users\gunal\Downloads\lake.jpeg")   # Replace with your image name

# Check if the image is loaded
if image is None:
    print("Error: Image not found!")
else:
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Display the original and outline images
    cv2.imshow("Original Image", image)
    cv2.imshow("Outline using Canny", edges)

    # Save the outline image
    cv2.imwrite("outline_photo.jpeg", edges)

    # Wait for a key press and close all windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()