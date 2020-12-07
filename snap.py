import picamera
from time import sleep


def snap():
    camera = picamera.PiCamera()
    counter = 0
    camera.capture("/home/pi/CS530PROJ/faces/headshot_1.jpg")
    
if __name__ == "__main__":
    snap()

#cam = cv2.VideoCapture(0)

#img_counter = 0
#last_time = time.time()
#while img_counter < 3:
#    cur_time = time.time()
#    ret, frame = cam.read()
#    if not ret:
#        print("failed to grab frame")
#        break
#    cv2.imshow("snap", frame)

#    k = cv2.waitKey(1)

#    if cur_time - last_time >= 3:
#        img_name = "new_user_pic_{}.png".format(img_counter)
#        cv2.imwrite(img_name, frame)
#        print("{} written!".format(img_name))
#        img_counter += 1
#        last_time = time.time()

#    if k % 256 == 27:
#        # ESC pressed
#        print("Escape hit, closing...")
#        break

#cam.release()
#cv2.destroyAllWindows()
