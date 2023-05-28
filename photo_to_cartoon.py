import cv2
import numpy as np
import sys

def main(arg):
    _img = cv2.imread(arg[1])

    # constrast stretching
    img = 255 / (200 - 20) * (_img.astype(np.int32) - 20)
    img = cv2.convertScaleAbs(img)

    # convert data shape to [N, 3]
    data = img.reshape((-1,3)).astype(np.float32)
    # Define criteria Max iter 10, acc 0.001, means 5
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 0.001)
    K = 5
    ret, label, center=cv2.kmeans(data, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res2 = res.reshape((img.shape))

    cv2.imwrite('res1.jpeg', res2)

    merge = np.hstack((res2, img))
    
    cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
    cv2.imshow('dst', merge)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    arg = sys.argv
    main(arg)