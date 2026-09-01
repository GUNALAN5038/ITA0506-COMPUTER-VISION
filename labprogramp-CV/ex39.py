import cv2

# Open the vehicle video
cap = cv2.VideoCapture(
        r"C:\Users\gunal\Downloads\CVLAB5.jpeg"

)

# Create background subtractor
bg_subtractor = cv2.createBackgroundSubtractorMOG2(
    history=500,
    varThreshold=50,
    detectShadows=False
)

# Check whether video is opened
if not cap.isOpened():
    print("Error: Video not found or cannot be opened!")
    exit()

while True:

    # Read one frame
    ret, frame = cap.read()

    # Stop when video ends
    if not ret:
        break

    # Apply background subtraction
    mask = bg_subtractor.apply(frame)

    # Remove small noise
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT,
        (5, 5)
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # Find contours
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # Detect objects
    for contour in contours:

        area = cv2.contourArea(contour)

        # Ignore small objects
        if area > 1000:

            x, y, w, h = cv2.boundingRect(contour)

            # Draw rectangle
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # Display label
            cv2.putText(
                frame,
                "Vehicle",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

    # Display result
    cv2.imshow(
        "Vehicle Detection",
        frame
    )

    # Press q to exit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

# Release video
cap.release()

# Close windows
cv2.destroyAllWindows()