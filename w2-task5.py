import cv2 as cv

capture = cv.VideoCapture("gandalfLaugh.mp4")

while True:

    retval, frame = capture.read()

    if not retval:
        break

    blur = cv.blur(frame, (5,5))
    blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)

    cv.imshow("Display name", blur)

    if cv.waitKey(17) == ord(' '): # close if spacebar is pressed
        break

capture.release()
cv.destroyAllWindows()