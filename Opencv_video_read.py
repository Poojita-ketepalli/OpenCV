import cv2

framewidth=640
frameheight=480

capture=cv2.VideoCapture(0)
capture.set(3,framewidth)
capture.set(4,frameheight)

while True:
    success,img=capture.read()
    cv2.imshow("Video",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break