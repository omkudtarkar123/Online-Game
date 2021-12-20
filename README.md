# Online-Game

* Requires python 3.10
* pip install pygame
* build docker image of server
  * docker build -t online-game .
* run docker
  * docker run -p 127.0.0.1:5555:5555 --rm -it online-game
* run client
  * python3 client.py
