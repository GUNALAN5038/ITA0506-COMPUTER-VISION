import cv2
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------
# LOAD IMAGE
# -------------------------------------------------

image = cv2.imread(
    r"C:\Users\gunal\Downloads\CVLAB5.jpeg"
)

if image is None:
    print("Error: Image not found. Check the file path.")
    exit()

# Convert BGR image to RGB
image_rgb = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2RGB
)

# Convert image to grayscale
gray = cv2.cvtColor(
    image,
    cv2.COLOR_BGR2GRAY
)


# -------------------------------------------------
# 1. HISTOGRAM EQUALIZATION
# -------------------------------------------------

equalized = cv2.equalizeHist(gray)


# -------------------------------------------------
# 2. CONTRAST ADJUSTMENT
# -------------------------------------------------

# Contrast factor
alpha = 1.5

# Brightness adjustment
beta = 0

contrast_adjusted = cv2.convertScaleAbs(
    gray,
    alpha=alpha,
    beta=beta
)


# -------------------------------------------------
# 3. SIFT FEATURE DETECTOR
# -------------------------------------------------

sift = cv2.SIFT_create()


# -------------------------------------------------
# 4. FEATURES FROM ORIGINAL IMAGE
# -------------------------------------------------

keypoints_original, descriptors_original = \
    sift.detectAndCompute(gray, None)

original_features = cv2.drawKeypoints(
    image_rgb,
    keypoints_original,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)


# -------------------------------------------------
# 5. FEATURES FROM HISTOGRAM-EQUALIZED IMAGE
# -------------------------------------------------

keypoints_equalized, descriptors_equalized = \
    sift.detectAndCompute(equalized, None)

equalized_rgb = cv2.cvtColor(
    equalized,
    cv2.COLOR_GRAY2RGB
)

equalized_features = cv2.drawKeypoints(
    equalized_rgb,
    keypoints_equalized,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)


# -------------------------------------------------
# 6. FEATURES FROM CONTRAST-ADJUSTED IMAGE
# -------------------------------------------------

keypoints_contrast, descriptors_contrast = \
    sift.detectAndCompute(
        contrast_adjusted,
        None
    )

contrast_rgb = cv2.cvtColor(
    contrast_adjusted,
    cv2.COLOR_GRAY2RGB
)

contrast_features = cv2.drawKeypoints(
    contrast_rgb,
    keypoints_contrast,
    None,
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)


# -------------------------------------------------
# 7. DISPLAY ENHANCEMENT RESULTS
# -------------------------------------------------

plt.figure(figsize=(15, 10))

# Original
plt.subplot(2, 3, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale")
plt.axis("off")

# Histogram Equalization
plt.subplot(2, 3, 2)
plt.imshow(equalized, cmap="gray")
plt.title("Histogram Equalization")
plt.axis("off")

# Contrast Adjustment
plt.subplot(2, 3, 3)
plt.imshow(contrast_adjusted, cmap="gray")
plt.title("Contrast Adjusted")
plt.axis("off")

# Original Features
plt.subplot(2, 3, 4)
plt.imshow(original_features)
plt.title("SIFT - Original")
plt.axis("off")

# Equalized Features
plt.subplot(2, 3, 5)
plt.imshow(equalized_features)
plt.title("SIFT - Histogram Equalized")
plt.axis("off")

# Contrast Features
plt.subplot(2, 3, 6)
plt.imshow(contrast_features)
plt.title("SIFT - Contrast Adjusted")
plt.axis("off")

plt.tight_layout()
plt.show()


# -------------------------------------------------
# 8. DISPLAY HISTOGRAMS
# -------------------------------------------------

plt.figure(figsize=(12, 5))

# Original Histogram
plt.subplot(1, 2, 1)

plt.hist(
    gray.ravel(),
    256,
    [0, 256]
)

plt.title("Original Image Histogram")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")


# Equalized Histogram
plt.subplot(1, 2, 2)

plt.hist(
    equalized.ravel(),
    256,
    [0, 256]
)

plt.title("Histogram After Equalization")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")

plt.tight_layout()
plt.show()


# -------------------------------------------------
# 9. FEATURE COUNT ANALYSIS
# -------------------------------------------------

print("---------------------------------------------")
print("       IMAGE ENHANCEMENT ANALYSIS")
print("---------------------------------------------")

print(
    "Original image SIFT keypoints:",
    len(keypoints_original)
)

print(
    "Histogram equalized SIFT keypoints:",
    len(keypoints_equalized)
)

print(
    "Contrast adjusted SIFT keypoints:",
    len(keypoints_contrast)
)

print("---------------------------------------------")

if len(keypoints_equalized) > len(keypoints_original):
    print(
        "Histogram equalization increased "
        "feature detection."
    )
else:
    print(
        "Histogram equalization did not increase "
        "feature detection."
    )

if len(keypoints_contrast) > len(keypoints_original):
    print(
        "Contrast adjustment increased "
        "feature detection."
    )
else:
    print(
        "Contrast adjustment did not increase "
        "feature detection."
    )

print("---------------------------------------------")
print("Experiment completed successfully.")
print("---------------------------------------------")
