import os
import time
import cv2
# import HandTrackingModule as htm
import hichemModule as htm

# j'ai du refaire un module sans la fonction de comptage de doight pour le faire fonctionner separement ici

wCam, hCam = 840, 540

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
#pour changer le luminosité id de ce parametre est 10
# cap.set(10, 100)
# # le param avec l'id 5 gere les fps
# cap.set(5, 120)

# folderPath = "FingerImages"
folderPath = "fingersTest"
myList = os.listdir(folderPath)
print(myList)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

# j'instancier le hand detector pour que je puisse l'utilisé
detector = htm.handDetector(detectionCon=0.6, maxHands=1)

tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 Fingers
        for id in range(1, 5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # print(222)
        totalFingers = fingers.count(1)
        print(" le nombre de doight levé est : ", (totalFingers))

        h, w, c = overlayList[totalFingers - 1].shape
        img[0:h, 0:w] = overlayList[totalFingers - 1]

        cv2.rectangle(img, (20, 325), (370, 625), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(totalFingers), (45, 475), cv2.FONT_HERSHEY_PLAIN,
                    10, (255, 0, 0), 25)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break