import cv2

# Load the pre-trained classifier
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Load an image
img = cv2.imread("example.jpg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = classifier.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

# Show the image
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()