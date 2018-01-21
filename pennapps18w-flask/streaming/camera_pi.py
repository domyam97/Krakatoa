import io
import picamera
from base_camera import BaseCamera
import time

class Camera(BaseCamera):
    global camera
    global kill
    kill = [0]
    @staticmethod
    def frames():
        global camera
        global kill
        time.sleep(2)
        camera = picamera.PiCamera()
        stream = io.BytesIO()
        for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield stream.read()

            stream.seek(0)
            stream.truncate()

            if(kill[0]):
                camera.close()
                kill[0] = 0
                break
                

    def close(self):
        global camera
        global kill
        kill[0] = 1
        
