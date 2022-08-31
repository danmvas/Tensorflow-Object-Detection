# importing cv2 
import cv2 
  
# path 
path = r'docker\test.jpg'
  
# Reading an image in default mode
image = cv2.imread(path)

# Using cv2.imshow() method 
# Displaying the image 
cv2.imshow('', image)


# Cropping an image
cropped_image = image[80:280, 150:330]

# Display cropped image
cv2.imshow("cropped", cropped_image)

  
#waits for user to press any key 
#(this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0) 
  
#closing all open windows 
cv2.destroyAllWindows() 