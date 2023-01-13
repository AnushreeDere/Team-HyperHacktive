import cv2
import face_recognition
import pickle
import os
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import wand

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{'databaseURL':"https://if-ps3-default-rtdb.firebaseio.com/",
                                    'storageBucket':"gs://if-ps3.appspot.com"  })

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

    fileN=os.path.join(folderPath,path)
    bucket=storage.bucket()
    blob=bucket.blob(fileN)
    blob.upload_from_filename(fileN)
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


