import cv2

framewidth=640
frameheight=480

capture=cv2.VideoCapture(0)
capture.set(3,framewidth)
capture.set(4,frameheight)

while True:
    success,img=capture.read()
    def sketch(x, y):
        return cv2.divide(x, 255 - y, scale=256)

    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Video",img_gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break