import cv2
import numpy as np
z = np.zeros((400,400,3),np.uint8)

cv2.line(z,(0,200),(400,200),(0,100,200),4)
cv2.rectangle(z,(10,10),(120,120),(0,0,200),2)
cv2.circle(z,(100,50),20,(0,200,0),2)
cv2.imshow("ventana",z)
cv2.waitKey(0)
cv2.destroyAllWindows()
