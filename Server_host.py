import socket
import sys
data = []

path = "file.txt"

num_of_client = 0

def read_txt(path):
    with open(path,'r') as file:
        data = file.read().split(' ')
        return data

def server_program(data):
    host = socket.gethostname()
    port = 5000

    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    conn, address = server_socket.accept()

    print("To connected user: " + str(data))

    conn.send(data.encode())
    conn.close()

def split():
    r =[]
    s=""
    n,i=0,0
    while(n<num_of_client):
        for i in range (n,len(data),num_of_client):
            if(i<len(data)):
                s+=data[i]
        n+=1
        r.append(s)
        s=""
    return r


if __name__ == '__main__':


    data =read_txt(path)

    print(f"Your messages: {data}")
    flage = True
    while(flage):
        try:
            num_of_client = int(input("Input num of clients: "))
            flage = False
        except ValueError:
            print("That's not an int!")
    lim = len(data)//num_of_client
    l_mes = (list(split()))
    for s in l_mes:
        server_program(s)
