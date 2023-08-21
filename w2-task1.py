import cv2 as cv
import numpy as np

def main():
    
    image = np.zeros([500, 500, 3])

    pt1 = (350,250)
    pt2 = (450,350)
    B, G, R =125, 50, 255
    colour = (B, G, R)
    points = np.array([[100, 100], [150, 50], [200, 100], [150, 150]], dtype=np.int32)

    cv.line(image, pt1, pt2, colour, 5)
    cv.rectangle(image, (150, 250), (250, 350), colour, 5)
    cv.circle(image, (425, 75), 50, colour, 5)  
    cv.polylines(image, [points], True, colour, 5)
    cv.putText(image, "hello world", (200, 200), cv.FONT_HERSHEY_SCRIPT_SIMPLEX, 2, colour, 1)

    cv.imshow('Image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()