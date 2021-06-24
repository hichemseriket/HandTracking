import cv2
import numpy as np
import time
from Pose import PoseModule as pm

cap = cv2.VideoCapture("AITrainer/1.mp4")

detector = pm.poseDetector()

while True:
    # success, img = cap.read()
    img = cv2.imread("AITrainer/1.jpg")
    # quand je mets Fals c'est que je veux plus qu'il dessine les connexion entre les points
    img = detector.findPose(img, False)
    img = cv2.resize(img, (720, 720))
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        detector.findAngle(img, 12, 14, 16)
    cv2.imshow("hichem", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
