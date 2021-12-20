FROM python:3

ADD server.py / 
ADD player.py /
ADD ball.py /

RUN pip3 install pygame

EXPOSE 5555 5555

CMD [ "python", "./server.py" ]