# make the video being photos
import cv2

capture = cv2.VideoCapture ('video.mp4')
frameNr = 0
while (True) :
    success , frame = capture.read ()

    if success :
        cv2.imwrite (f'C:/Users/irene/PycharmProjects/m frame_{frameNr}.jpg' , frame)

    else :
        break

    frameNr = frameNr + 1
capture.release ()
