import cv2


img = cv2.imread('Dhoni-2.jpg')
img=cv2.resize(img,(400,600))

def sketch(x, y):
    return cv2.divide(x, 255 - y, scale=256)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_invert = cv2.bitwise_not(img_gray)
img_smoothing = cv2.GaussianBlur(img_invert, (21, 21),sigmaX=0, sigmaY=0)
final_img = sketch(img_gray, img_smoothing)
cv2.imshow('Image',final_img)

cv2.waitKey(0)
