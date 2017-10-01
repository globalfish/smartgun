import numpy as np
import cv2
import sys

if( len(sys.argv) < 4 ):
    print("Usage: ",sys.argv[0], " username password cameraIP")
    quit()

cameraIP = sys.argv[3]
user= sys.argv[1]
password = sys.argv[2]
userauth = (user, password)
streamurl = "http://" + ':'.join(userauth) + '@' + cameraIP + "/video1.mjpg"
print("Invoking URL: ", streamurl)
print("Press 'q' to quit...")
cap = cv2.VideoCapture(streamurl)

while(cap.isOpened()):
    ret, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame',frame)
    #cv2.imshow('gray',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
