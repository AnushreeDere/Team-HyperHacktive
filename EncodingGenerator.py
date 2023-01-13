import cv2
import face_recognition
import pickle
import os

#Importing student images
folderPath="Images"
pathList=os.listdir(folderPath)
print(pathList)
imgList=[]
studentIds=[]
#print(modePathList)
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    #print(path)#prints 211081030.png --> we need to remove .png
    #print(os.path.splitext(path)) #--> gives '211081030', '.jpg'
    #print(os.path.splitext(path)[0])#we take only 1st element:regid,and discard .jpg
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagesList):
    encodeList=[]
    for img in imagesList:
        img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #facerec uses rgb opencv uses bgr
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList

print("Encoding started")
encodeListKnown=findEncodings(imgList)
encodeListwithIds=[encodeListKnown, studentIds]
print("Encoding Done")

myfile=open("EncodeFile.p",'wb') #p file is a pickle file
pickle.dump(encodeListwithIds,myfile)
myfile.close()
print("File saved")
