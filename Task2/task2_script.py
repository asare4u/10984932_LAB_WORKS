import cv2
import matplotlib.pyplot as plt

# Load the color image
color_image = cv2.imread('photo.jpg')

# Check if the image was loaded successfully
if color_image is None:
    print("Error: Could not load the image. Please ensure 'photo.jpg' is in the same directory.")
else:
    # Convert to different color spaces
    grayscale_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    hsv_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2HSV)
    lab_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2LAB)

    # Display each image
    cv2.imshow('Original Image', color_image)
    cv2.imshow('Grayscale Image', grayscale_image)
    cv2.imshow('HSV Image', hsv_image)
    cv2.imshow('LAB Image', lab_image)

    # Save each converted image
    cv2.imwrite('photo_grayscale.jpg', grayscale_image)
    cv2.imwrite('photo_hsv.jpg', hsv_image)
    cv2.imwrite('photo_lab.jpg', lab_image)

    # Plot the histogram of the grayscale image
    plt.hist(grayscale_image.ravel(), 256, [0, 256])
    plt.title('Grayscale Image Histogram')
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Frequency')
    plt.show()

    # Wait for a key press and close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()