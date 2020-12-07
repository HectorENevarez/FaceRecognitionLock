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

    f = open("./faces/headshot_1.jpg", 'rb')

    l = f.read(40960000)
    s.send(l)

    f.close()
    print("Done Sending")

    result = s.recv(1024)

    result = result.decode()
    print("result received!", result)
    return result



# if __name__ == "__main__":
#     #server_program()
#     client_program()
