from flask import Flask, render_template, Response
from camera_pi import Camera
import picamera
import time
import logging
from detect import detectFaces, uploadFile

# Setup logging
logger = logging.getLogger('mainlog')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

app = Flask(__name__)

run = [1]


@app.route('/')
def index():
    return render_template('index.html')

def gen(camera):
    logger.debug('generated camera')
    while run[0]:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
    camera.close()
    logger.debug("Camera actually killed")

@app.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
        mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/arbitrary_name', methods=['POST'])
def arbitrary_name():
    try:
        # Take video
        logger.info('Getting ready for video')
        run[0] = 0
        logger.debug("Killed camera")
        time.sleep(5)
        camera = picamera.PiCamera()
        logger.debug("Started camera")
        filename = time.strftime('%y-%m-%d_%H-%M.h264')
        logger.debug(camera)
        camera.start_recording('./tmp/'+filename)
        logger.debug("Starting video...")
        time.sleep(1)
        camera.stop_recording()
        logger.debug("Stopped recording")

        uploadFile(filename)
        logger.debug("Uploaded")
        detectFaces(filename)
        logger.debug("Faces found")
    except Exception as e:
        logger.error(traceback.format_exc())

    # Redirect to video_feed
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
