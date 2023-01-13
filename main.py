import cv2
import os

cap=cv2.VideoCapture(0)
cap.set(3,350)
cap.set(4,400)

imgBackground=cv2.imread("Resources/11.jpg")

#Importing the mode images into a list
folderModePath="Resources/Modes"
modePathList=os.listdir(folderModePath)
imgModeList=[]
#print(modePathList)
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath,path)))
#print(len(imgModeList))

while (True):
    success, img=cap.read()
    imgBackground[202:202+288,48:48+352]=img
    imgBackground[490:490+139,56:56+248]=imgModeList[1]
    #cv2.imshow("Webcam",img)
    cv2.imshow("Face Attendance",imgBackground)
    if cv2.waitKey(1)& 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    
