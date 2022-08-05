from typing import List
from pydantic import BaseSettings
from datetime import datetime

import cv2
import threading
import time

class Settings(BaseSettings):
    cameras: List[dict]

    class Config:
        env_file = ".env.recording"
settings = Settings()

class camThread(threading.Thread):
    def __init__(self, previewName, camID):
        threading.Thread.__init__(self)
        self.previewName = previewName
        self.camID = camID
    def run(self):
        print("Starting " + self.previewName)
        camPreview(self.previewName, self.camID)

def camPreview(previewName, camID):
    cam = cv2.VideoCapture(camID)
    if cam.isOpened():  # try to get the first frame
        rval, frame = cam.read()
    else:
        rval = False

    while not rval:
        rval, frame = cam.read()

    
    frame = cv2.resize(frame, (1280, 720))
    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
    writer = cv2.VideoWriter(previewName+".avi", fourcc, 12, (frame.shape[1], frame.shape[0]), True)

    while True:
        rval, frame = cam.read()

        if(rval):
            frame = cv2.resize(frame, (1280, 720))
            if writer is not None:
                writer.write(frame)

        time.sleep(0.100)

        #key = cv2.waitKey(20)
        #if key == 27:  # exit on ESC
            #break

    # writer.release()

    # cv2.destroyWindow(previewName)

for i, v in enumerate(settings.cameras):
    date = datetime.now().strftime("%Y%m%d%I%M%S")
    print (date + ' ' + v["source"])
    thread = camThread(date, v["source"])
    thread.start()
    time.sleep(0.25)
#thread1 = camThread("Camera01", "rtsp://admin:Prime@itapoa@192.168.5.31:554/Streaming/Channels/1")
#thread2 = camThread("rtsp://admin:Prime@itapoa@192.168.5.29:554/Streaming/Channels/1", 2)

#thread1.start()

