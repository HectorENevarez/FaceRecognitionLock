import socket
from PIL import Image
import face_detection_small

def server_programs():
    host = '0.0.0.0'
    port = 2345
    s = socket.socket()
    s.bind((host, port))
    f = open('torecv.raw', 'wb')
    s.listen(5)
    c, addr = s.accept()
    print("Got connection from: ", addr)
    
    l = c.recv(1024)
    while:
        print('Recieving')
        f.write(l)
        l = c.recv(1024)

    f.close()
    print("Done Recieving")

    print("Converting raw Image...")
    im = Image.open("torecv.raw")
    rgb_im = im.convert('RGB')
    rgb_im.save("converted.jpg")
    print("Image has been converted to jpg")
    rawData = open("torecv.txt", 'rb').read()
    imgSize = (854, 642)
    img = Image.frombytes('L', imgSize, rawData)
    img.save("torecv.png")

    result = face_detection_small.classify_face("converted.jpg")[0]
    print("sending result")
    c.send(str(result).encode())

    c.close()

if __name__ == '__main__':
    server_program() #Direct call
