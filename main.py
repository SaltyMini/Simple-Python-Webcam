import cv2
from tkinter import messagebox

messagebox.showinfo(title="INFO", message="Press Q to quit")

cv2.startWindowThread()
cam = cv2.VideoCapture(0)

frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')


while True:
    ret, frame = cam.read()
    cv2.imshow('Camera', frame)

    if cv2.waitKey(1) == ord('q'):
        break
    
cam.release()
cv2.destroyAllWindows()