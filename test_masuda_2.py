import time
import picamera
with picamera.PiCamera() as camera:
    camera.start_preview()
    time.sleep(2)
    camera.capture_sequence([
        '/home/pi/nas/photo/test_masuda_image1.jpg',
        '/home/pi/nas/photo/test_masuda_image2.jpg',
        '/home/pi/nas/photo/test_masuda_image3.jpg',
        ])
    camera.stop_preview()
