from detect import uploadFile
import detect
import time

import picamera
'''
camera = picamera.PiCamera()
filename = time.strftime('%y-%m-%d_%H-%M.h264')
print("STARTING")
camera.start_recording('./tmp/'+filename)
time.sleep(10)
camera.stop_recording()

print("DONE")
'''
uploadFile('18-01-21_01-25.h264')
