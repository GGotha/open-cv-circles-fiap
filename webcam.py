#!/usr/bin/python

import cv2
import numpy as np

rval = True

while rval:
    img = cv2.imread('./circulo.png')

    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        for (x, y, r) in circles:
            circleArea = 2 * (3.14 * r)
            circleAreaFormatted = "A: "+"{:.2f}".format(round(circleArea, 2))

            if (r != 84):
                cv2.circle(output, (x, y), r, (0, 255, 0), 4)
                cv2.putText(output, circleAreaFormatted, (x - 75,y - 40), font, 1, (0, 0, 0))
                cv2.putText(output, "CM", (x - 10, y - 10), font, .5, (0, 0, 0))
                cv2.circle(output, (x, y), 6, (0, 0, 0), -1)
        cv2.imshow("output", output)
        key = cv2.waitKey(20)
        if key == 27:
            break

    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.destroyWindow("output")

