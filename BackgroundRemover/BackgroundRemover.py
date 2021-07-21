import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
# pour augmenter les fps
cap.set(cv2.CAP_PROP_FPS, 60)

segmentor = SelfiSegmentation()
fpsReader = cvzone.FPS()

imgBG = cv2.imread("images/flamme.jpg")

listImg = os.listdir("images")
imgList = []
print(listImg)
for imgPath in listImg:
    img = cv2.imread(f"images/{imgPath}")
    imgList.append(img)
print(len(listImg))

indexImg = 0
while True:
    success, img = cap.read()

    # l'option treshold est ici pour mieux decoupé le personnage du BG, a 0.8 elle me parrait coupe bien
    imgOut = segmentor.removeBG(img, imgList[indexImg], threshold=0.5)

    imgStacked = cvzone.stackImages([imgOut, img], 2, 1)
    _, imgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))
    cv2.imshow("hichem", imgStacked)
    # cv2.imshow("hichem", img)
    # cv2.imshow("NoBG", imgOut)
    cv2.imshow("moi", imgOut)
    key = cv2.waitKey(1) & 0xFF

    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList) - 1:
            indexImg += 1
    elif key == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
