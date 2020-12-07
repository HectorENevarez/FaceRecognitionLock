import socket
from PIL import Image
import face_detection_small


# 192.168.0.103
def client_program():
    host = '192.168.0.75'  # as both code is running on same pc
    port = 2345  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = input(" -> ")  # take input

    while message.lower().strip() != 'bye':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response

        print('Received from server: ' + data)  # show in terminal

        message = input(" -> ")  # again take input

    client_socket.close()  # close the connection


def server_program():
    host = '0.0.0.0'
    port = 2345
    s = socket.socket()
    s.bind((host, port))
    f = open('torecv.raw', 'wb')
    s.listen(5)

    c, addr = s.accept()
    print("Got connection from: ", addr)
    l = c.recv(40960000)
    f.write(l)
    print("test")
    f.close()
    print("Done Recieving")
    # c.send(b"Thank you for connecting")


    print("Converting raw Image...")
    im = Image.open("torecv.raw")
    rgb_im = im.convert('RGB')
    rgb_im.save("converted.jpg")
    print("Image has been converted to jpg")
    # rawData = open("torecv.txt", 'rb').read()
    # imgSize = (854, 642)
    # img = Image.frombytes('L', imgSize, rawData)
    # img.save("torecv.png")

    result = face_detection_small.classify_face("converted.jpg")
    print("sending result")
    c.send(str(result).encode())

    c.close()

if __name__ == '__main__':
    # client_program()
    server_program()

