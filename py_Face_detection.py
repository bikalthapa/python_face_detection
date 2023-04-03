# A program to detect face in python 
import cv2
face_cap = cv2.CascadeClassifier("C:/Users/subash/AppData/Local/Programs/Python/Python310/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

#Enabling camera recording
video_cap = cv2.VideoCapture(0)

# Running camera for infinite 
while True:
    # Reading images from camera
    a, video = video_cap.read()
    col = cv2.cvtColor(video,cv2.COLOR_BGR2GRAY)
    # covering face
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor = 1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    # making rectangle
    for (x,y,w,h) in faces:
        cv2.rectangle(video,(x,y),(x+w, x+h), (0,255,0),2)
    cv2.imshow("Bikal's Camera",video)
    # Taking exit from infinite loop if a is pressed in keyboard
    if cv2.waitKey(10) == ord("a") :
        break
video_cap.release()