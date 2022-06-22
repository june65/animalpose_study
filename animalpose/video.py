import numbers
import cv2
from animalpose import *

cap = cv2.VideoCapture("input.mp4")

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

i=1
while (cap.isOpened):

    ret, frame = cap.read()

    if ret:

        cv2.imshow("video", frame)

        k = cv2.waitKey(3000)

        cv2.imwrite("input/input"+ str(i).zfill(3) +".png", frame)
        f = open("number.txt", 'w')
        f.write(str(i).zfill(3))
        f.close()
        
        main()

        if k == 27:

            break
        i=i+1
    else:

        break

cap.release()

cv2.destroyAllWindows()