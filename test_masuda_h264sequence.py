import picamera
with picamera.PiCamera() as camera:
    for filename in camera.record_sequence(
            'clip%02d.h264' % i for i in range(3)):
        print('Recording to %s' % filename)
        camera.wait_recording(10)

        