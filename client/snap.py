import picamera
from time import sleep


def snap():
    camera = picamera.PiCamera()
    camera.capture("/home/pi/CS530PROJ/faces/headshot_1.jpg")

if __name__ == "__main__":
    snap()
