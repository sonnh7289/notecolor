import numpy as np
import cv2
from cartoonize import caart




videoCaptureObject = cv2.VideoCapture(0)

out = cv2.VideoWriter('out.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 24, (720, 1280))
result = True
while(result):
    ret,img = videoCaptureObject.read()
    img=caart(img)
    cv2.imshow("original",np.array(img))
    out.write(img)
    # if(cv2.waitKey(27) & 0xFF==27):
    #     break
    if(cv2.waitKey(1) & 0xFF==ord('q')):
        break
videoCaptureObject.release()
cv2.destroyAllWindows()