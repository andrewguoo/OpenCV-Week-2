import cv2 as cv
import matplotlib.pyplot as plt

def main():

    image = cv.imread("OpenCV-Week-2\images\park.png")
    blur = cv.blur(image, (5,5))
    gaussian = cv.GaussianBlur(image, (5,5), 0)
    median = cv.medianBlur(image, 5)
    bilateral = cv.bilateralFilter(image, 25, 75, 75)

    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    blur = cv.cvtColor(blur, cv.COLOR_BGR2RGB)
    gaussian = cv.cvtColor(gaussian, cv.COLOR_BGR2RGB)
    median = cv.cvtColor(median, cv.COLOR_BGR2RGB)
    bilateral = cv.cvtColor(bilateral, cv.COLOR_BGR2RGB)

    plt.subplot(231), plt.imshow(image), plt.title("Original")

    plt.xticks([]), plt.yticks([])

    plt.subplot(232), plt.imshow(blur), plt.title("Average")

    plt.xticks([]), plt.yticks([])

    plt.subplot(233), plt.imshow(gaussian), plt.title("Gaussian")

    plt.xticks([]), plt.yticks([])

    plt.subplot(234), plt.imshow(median), plt.title("Median")

    plt.xticks([]), plt.yticks([])

    plt.subplot(235), plt.imshow(bilateral), plt.title("Bilateral")

    plt.xticks([]), plt.yticks([])

    plt.suptitle("Types of Blur")

    plt.tight_layout()

    plt.show()


if __name__=="__main__":
    main()