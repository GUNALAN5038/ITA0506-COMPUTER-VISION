import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# Load Image
# -------------------------------------------------

image = cv2.imread(r"C:\Users\gunal\Downloads\CVLAB5.jpeg")

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# -------------------------------------------------
# HARRIS CORNER DETECTION
# -------------------------------------------------

# Convert grayscale image to float32
gray_float = np.float32(gray)

# Apply Harris Corner Detection
harris = cv2.cornerHarris(
    gray_float,
    blockSize=2,
    ksize=3,
    k=0.04
)

# Dilate the corner response for better visibility
harris = cv2.dilate(harris, None)

# Create a copy for displaying Harris corners
harris_image = image.copy()

# Set threshold for strong corners
threshold = 0.01 * harris.max()

# Mark detected Harris corners in red
harris_image[harris > threshold] = [0, 0, 255]


# -------------------------------------------------
# SIFT FEATURE DETECTION
# -------------------------------------------------

# Create SIFT detector
sift = cv2.SIFT_create()

# Detect SIFT keypoints and descriptors
keypoints, descriptors = sift.detectAndCompute(
    gray,
    None
)

# Draw SIFT keypoints
sift_image = cv2.drawKeypoints(
    image,
    keypoints,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)


# -------------------------------------------------
# CONVERT BGR TO RGB FOR MATPLOTLIB
# -------------------------------------------------

original_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

harris_rgb = cv2.cvtColor(
    harris_image,
    cv2.COLOR_BGR2RGB
)

sift_rgb = cv2.cvtColor(
    sift_image,
    cv2.COLOR_BGR2RGB
)


# -------------------------------------------------
# DISPLAY RESULTS
# -------------------------------------------------

plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(original_rgb)
plt.title("Original Image")
plt.axis("off")

# Harris Corner Detection
plt.subplot(1, 3, 2)
plt.imshow(harris_rgb)
plt.title("Harris Corner Detection")
plt.axis("off")

# SIFT Keypoints
plt.subplot(1, 3, 3)
plt.imshow(sift_rgb)
plt.title("SIFT Keypoints")
plt.axis("off")

plt.tight_layout()
plt.show()


# -------------------------------------------------
# DISPLAY SIFT INFORMATION
# -------------------------------------------------

print("-----------------------------------------")
print("        SIFT FEATURE INFORMATION")
print("-----------------------------------------")

print("Number of SIFT keypoints detected:",
      len(keypoints))

if descriptors is not None:
    print("SIFT descriptor shape:",
          descriptors.shape)
else:
    print("No SIFT descriptors were detected.")

print("-----------------------------------------")
print("Experiment completed successfully.")
print("-----------------------------------------")