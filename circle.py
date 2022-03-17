#!/usr/bin/python

from black import out
import cv2
import numpy as np
import math

rval = True

while rval:
    img = cv2.imread('./circulo.png')

    output = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

    font = cv2.FONT_HERSHEY_SIMPLEX

    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")

        XrightCircle = circles[0][0]; 
        YrightCircle = circles[0][1]; 
        RrightCircle = circles[0][2]; 

        XleftCircle = circles[1][0]; 
        YleftCircle = circles[1][1]; 
        RleftCircle = circles[1][2]; 

        for (x, y, r) in circles:
            circleArea = 2 * (3.14 * r)
            circleAreaFormatted = "A: "+"{:.2f}".format(round(circleArea, 2))

            angle = int(math.degrees(math.atan2(YleftCircle - YrightCircle,XleftCircle - XrightCircle))) * -1
            angleFormatted = "{}{}".format("Angulo:", angle)

            textsize = cv2.getTextSize(angleFormatted, font, 1, 2)[0]
            textX = (output.shape[1] - textsize[0]) / 2
            textY = (output.shape[0] + textsize[1]) / 2


            isACircle = r > 100

            if (isACircle):
                cv2.putText(output, angleFormatted, (int(textX), int(textY - 100)), font, 1, (0, 0, 0), 2)
                cv2.line(output, (XrightCircle, YrightCircle), (XleftCircle, YleftCircle), (255, 0, 0), 4)
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

