import cv2
import pyttsx3

thres = 0.5 #Threshold to detect objects

cap = cv2.VideoCapture(1)
cap.set(3,640)
cap.set(4,480)


classNames=[]
classFile='coco.names'
with open(classFile,'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

weightsPath = 'frozen_inference_graph.pb'
configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

while True:
    success,img = cap.read()
    classIds, confs, bbox = net.detect(img,confThreshold=thres)




    if len(classIds) !=0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            cv2.rectangle(img,box,color=(0,255,0),thickness=2)
            cv2.putText(img,classNames[classId-1].upper(),(box[0]+10,box[1]+30),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)

            cv2.putText(img, str(round(confidence*100,2)), (box[0] + 200, box[1] + 30), cv2.FONT_HERSHEY_COMPLEX, 1,
                        (0, 255, 0), 2)



            #txt=classNames[classId - 1]


    cv2.imshow("Output", img)                         #In this three line i applied stop function
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


txt=classNames[classId-1]

engine = pyttsx3.init()
engine.say(f"Object is, {txt}")
engine.setProperty("rate", 50)
engine.runAndWait()

