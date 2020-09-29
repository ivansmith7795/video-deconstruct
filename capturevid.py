import cv2
import time
import os
import shutil

from pathlib import Path
from shutil import copyfile

rtsp_ip = "10.48.6.186"
rtsp_user = "root"
rtsp_password = "Nutrien123!"
rtsp_camera_stream = "rtsp://" + rtsp_user + ":" + rtsp_password + "@" + rtsp_ip + "/axis-media/media.amp"
streamname = "aln-underground-belt-54"
temp_path = "frames"

def readstream():
    
    vcap = cv2.VideoCapture(rtsp_camera_stream)
    
    raw_path = temp_path + "/raw/" + streamname

    #Delete the temp map directory if it already exists
    if os.path.isdir(raw_path) == True:
        shutil.rmtree(raw_path)

    count = 0

    while(True):
        count = count + 1
        ret, frame = vcap.read()
        
        #Check if temp directory exists, if no create
        Path(raw_path).mkdir(parents=True, exist_ok=True)
        
        timestart = time.perf_counter()

        if frame is not None:
              
            cv2.imwrite(raw_path +"/frame" + str(count) + ".png", frame)

        else:
            print("Frame is empty, video disconnect. Restablishing connection...")
            vcap.release()
            print("Video stopped")
            print("Reinitializing")
            count = 0
            readstream()
            break

        timeend = time.perf_counter()
        #print(f"Inference took {timeend - timestart:0.4f} seconds")

    # When everything done, release the capture
    print("Capture complete")
    vcap.release()
    cv2.destroyAllWindows()


readstream()