import cv2

# Read the image
img = cv2.imread(
        r"C:\Users\gunal\Downloads\CVLAB5.jpeg"

)

# Check whether image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Make a copy of the original image
result = img.copy()

# Convert image to grayscale
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# Apply binary threshold
_, thresh = cv2.threshold(
    gray,
    120,
    255,
    cv2.THRESH_BINARY
)

# Find contours
contours, _ = cv2.findContours(
    thresh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

count = 0

# Process each contour
for contour in contours:

    # Calculate area
    area = cv2.contourArea(contour)

    # Ignore very small objects
    if area > 500:

        # Get bounding rectangle
        x, y, w, h = cv2.boundingRect(contour)

        # Draw rectangle
        cv2.rectangle(
            result,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Extract object
        object_image = img[
            y:y + h,
            x:x + w
        ]

        count = count + 1

        # Display extracted object
        cv2.imshow(
            "Extracted Object " + str(count),
            object_image
        )

# Display number of objects
print("Number of objects detected:", count)

# Display final image
cv2.imshow(
    "Objects with Rectangular Boxes",
    result
)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()