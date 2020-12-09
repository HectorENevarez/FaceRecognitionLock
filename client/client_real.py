import socket

def client_program():
    host = "192.168.0.30"
    port = 2345

    s = socket.socket()
    s.connect((host, port))

    f = open("./faces/headshot_1.jpg", 'rb')
    l = f.read(1024)

    while(l):
        print('Sending...')
        s.send(l)
        l = f.read(1024)

    f.close()
    print("Done Sending")

    result = s.recv(1024)

    result = result.decode()
    print("result received!", result)
    return result



if __name__ == "__main__":
    client_program()
