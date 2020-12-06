import socket
HOST = 'localhost'
PORT = 10000
def echo_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while True:
        filename = '/Users/apple/Desktop/echo/test.txt'
        with open (filename, 'rb') as f:
            s.sendfile(f)
        data = s.recv(1024)
        if not data:
            break
        else:
            print(data.decode('utf-8'))
    s.close()
if __name__ == '__main__':
    echo_client()
