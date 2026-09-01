import cv2

# Load Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Read the image
img = cv2.imread(
        r"C:\Users\gunal\Downloads\CVLAB5.jpeg"

)

# Check if image is loaded
if img is None:
    print("Error: Image not found!")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    minSize=(30, 30)
)

# Draw rectangles around detected faces
for (x, y, w, h) in faces:

    cv2.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        2
    )

    cv2.putText(
        img,
        "Face",
        (x, y - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

# Print number of faces
print("Number of faces detected:", len(faces))

# Display result
cv2.imshow(
    "Face Detection",
    img
)

# Wait for key press
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()