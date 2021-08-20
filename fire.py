import numpy as np
import cv2

def main():
    img = cv2.imread('picture/fire.jpg')
    print(np.shape(img))


if __name__ == '__main__':
    print("Hello world!")
    main()
