import socket, sys
from _thread import *
from player import Player
import pickle
from ball import Ball

#server = "192.168.86.62"
#server = "127.0.0.1"
server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print('Waiting for a connection\nServer Started')

    
players = [Player(200,0,100,25,(255,0,0)), Player(200,475,100,25,(0,0,255)), Ball(250,250,25, (0,0,0)), Ball(250,250,25, (0,0,0))]
#ball = Ball(250,250,25, (0,0,0))

def threaded_client(conn, player):
    conn.send(pickle.dumps((players[player], players[2])))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data[0]
            players[2] = data[1]
            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = (players[0], players[2])
                else:
                    reply = (players[1], players[2])
                print("Received: ", data)
                print("Sending:", reply)
            conn.sendall(pickle.dumps(reply))
        except:
            break
    print('Lost connections')
    conn.close()

currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1

