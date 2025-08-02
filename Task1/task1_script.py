import cv2

# Load the image
original_image = cv2.imread('photo.jpg')

# Check if the image was loaded successfully
if original_image is None:
    print("Error: Could not load the image. Please ensure 'photo.jpg' is in the same directory.")
else:
    # Convert the image to grayscale
    grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)

    # Display the original and grayscale images
    cv2.imshow('Original Image', original_image)
    cv2.imshow('Grayscale Image', grayscale_image)

    # Save the grayscale image
    cv2.imwrite('photo_gray.jpg', grayscale_image)

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()