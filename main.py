import cv2

# get the image location and the image file name
img_location = 'C:/Users/lelon/Desktop/'
filename = 'Long.jpg'

# Read in the image
img = cv2.imread(img_location+filename)

# Convert the image to grayscale
gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Invert the image
inverted_gray_image = 255 - gray_image

# Blur the image by gaussian function
blurred_image = cv2.GaussianBlur(inverted_gray_image, (21,21), 0)

# Invert the blurred image
inverted_blurred_image = 255 - blurred_image

# Create the pencil sketch image
pencil_sketch_image = cv2.divide(gray_image, inverted_blurred_image, scale=256.0)

# Show the image
cv2.imshow('Pencil Sketch Image', pencil_sketch_image)
cv2.waitKey(0)

