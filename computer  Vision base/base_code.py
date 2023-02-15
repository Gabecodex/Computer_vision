import cv2

# Load the image
img = cv2.imread("image.png")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply a Gaussian blur to the image
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)

# Detect edges in the image using Canny edge detection
edged_img = cv2.Canny(blurred_img, 30, 150)

# Display the original and processed images
cv2.imshow("Original Image", img)
cv2.imshow("Edged Image", edged_img)
cv2.waitKey(0)
cv2.destroyAllWindows()