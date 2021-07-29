import os
import time
import cv2
import mediapipe as mp

# import HandTrackingModule as htm
import hichemModule as htm

# j'ai du refaire un module sans la fonction de comptage de doight pour le faire fonctionner separement ici

wCam, hCam = 1400, 1000

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# pour changer le luminosité id de ce parametre est 10
# cap.set(10, 100)
# # le param avec l'id 5 gere les fps
# cap.set(5, 120)

# folderPath = "../FingerImages"
folderPath = "../fingersTest"
myList = os.listdir(folderPath)
print(myList)
overlayList = []

#####################################################
# gestion visage

pTime = 0

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2)

# si video hd , j'augmente la thikness et le rayon des cercle ici
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1)
#################################

for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

print(len(overlayList))
pTime = 0

detector = htm.handDetector(detectionCon=0.6, maxHands=1)

tipIds = [4, 8, 12, 16, 20]
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                print(id, cx, cy)
                if id == 4 or id==8 or id==12 or id==16 or id==20:
                    cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (400, 70), cv2.FONT_HERSHEY_PLAIN,
                3, (255, 0, 0), 3)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
