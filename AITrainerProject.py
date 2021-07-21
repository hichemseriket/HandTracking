import cv2
import numpy as np
import moviepy.editor as mop

import time
from Pose import PoseModule as pm
##################################
width = 860
height = 640
##################################

cap = cv2.VideoCapture("AITrainer/6.mp4")

# tous ce code en bas est la pour convertir les video en plus petite resolution
# clip = mop.VideoFileClip("AITrainer/1.mp4")
# clip_resized = clip.resize(height=680) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("AItrainer/5.mp4")
# clip = mop.VideoFileClip("AITrainer/2.mp4")
# clip_resized = clip.resize(height=680) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("AItrainer/6.mp4")
# clip = mop.VideoFileClip("AITrainer/3.mp4")
# clip_resized = clip.resize(height=680) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("AItrainer/7.mp4")
# clip = mop.VideoFileClip("AITrainer/4.mp4")
# clip_resized = clip.resize(height=680) # make the height 360px ( According to moviePy documenation The width is then computed so that the width/height ratio is conserved.)
# clip_resized.write_videofile("AItrainer/8.mp4")
# cap.set(3, width)
# cap.set(4, height)
detector = pm.poseDetector()
count = 0
dir = 0
pTime = 0

while True:
    success, img = cap.read()
    # img = cv2.resize(img, (680, 480))

    # cap.set(3, width)
    # cap.set(4, height)
    # img = cv2.imread("AITrainer/1.jpg")
    # quand je mets Fals c'est que je veux plus qu'il dessine les connexion entre les points
    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        # Right Arm
        angle = detector.findAngle(img, 12, 14, 16)
        # Left Arm
        # angle = detector.findAngle(img, 11, 13, 15)
        # je transform en pourcentage l'angle correct de
        # l'exercice poids avec main gauche
        # l'exercice doit etre fait avec le bras gauche et de profil
        # per = np.interp(angle, (210, 310), (0, 100))
        # selon la video black fait des bras les limites sont :
        per = np.interp(angle, (190, 330), (0, 100))
        # print(angle, per)

        # Check for the dumbbell curls, un exercice complet

        if per == 100:
            # verifier si la direction up
            if dir == 0:
                # je rajoute 0.5 au compteur
                count += 0.5
                dir = 1
        if per == 0:
            if dir == 1:
                count += 0.5
                dir = 0
        print(count)
        cv2.putText(img, str(int(count)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (50, 100), cv2.FONT_HERSHEY_PLAIN, 5, (255, 0, 0), 5)

    cv2.imshow("hichem", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()
