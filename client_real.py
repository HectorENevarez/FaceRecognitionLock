import socket


def server_program():
    host = '0.0.0.0'
    port=2345

    server_socket = socket.socket()
    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()
    print("Connection from: " + str(address))

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print("From connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()


def client_program():
    host = "192.168.0.103"
    port = 2345

    s = socket.socket()
    s.connect((host, port))

    f = open("guadiana_face.jpg", 'rb')    

    l = f.read(1024)
    while(l):
        print("Sending...")
        s.send(l)
        l = f.read(1024)

    f.close()
    print("Done Sending")
    s.close()


if __name__ == "__main__":
    #server_program()
    client_program()