import cv2
import os 

img1 = cv2.imread("Lesson 1 /images/flower.jpeg")
cv2.imshow("opencv", img1)
cv2.waitKey(0)

img2 = cv2.imread("Lesson 1 /images/flower.jpeg",0)
cv2.imshow("opencv",img2)
cv2.waitKey(0)

"""
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

img2 = cv2.imread("Lesson 1 /images/flower.jpeg",0)
cv2.imshow("opencv",img2)
cv2.waitKey(0)

# Save the image after changes
cv2.imwrite("gray.png",img2)

# OS methods
print(os.getcwd())
path = "/Users/ishwa/Documents"
os.chdir(path)
cv2.imwrite("gray.png",img2)

# spliting into BGR(blue, green red)
B,G,R = cv2.split(img1)
cv2.imshow("opencv",B)
cv2.waitKey(0)

cv2.imshow("opencv",G)
cv2.waitKey(0)

cv2.imshow("opencv",R)
cv2.waitKey(0)
"""

print(img1.shape)
print(img2.shape)

img3 = img1[500:600,500:700]
cv2.imshow("opencv",img3)
cv2.waitKey(0)

# check for the BGR values at a particular point 
i,j = 50,400
print(img1[i,j])