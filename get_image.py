from picamera import PiCamera
import time

camera = PiCamera()

camera.start_preview()
time.sleep(2)
camera.capture('/home/pi/CS530PROJ/image.jpg')
camera.stop_preview()