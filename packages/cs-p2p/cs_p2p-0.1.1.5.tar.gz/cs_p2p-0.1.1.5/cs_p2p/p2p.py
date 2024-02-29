import os
import queue
import zmq
import time
import threading

from dotenv import load_dotenv

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
SERVER_IP = os.getenv("SERVER_IP")

def __publisher(channel, text):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://{SERVER_IP}:{ZMQ_PORT}")
    
    print(f"Pubblicazione sul canale '{channel}': {text}")
    socket.send_string(f"{channel} {text}")
   

def publish(channel, text):
    zmq_publisher_thread = threading.Thread(target=__publisher, args=(channel, text))
    zmq_publisher_thread.start()

def __subscriber(channel, ip_address):
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect(f"tcp://{ip_address}:{ZMQ_PORT}")  # Accetta connessioni da tutti gli indirizzi IP
    socket.setsockopt_string(zmq.SUBSCRIBE, f"{channel} ")  # Sottoscrivi a tutti i messaggi

    while True:
        messaggio = socket.recv_string()
        canale_ricevuto, testo = messaggio.split(" ", 1)
        print(f"Ricevuto dal canale '{canale_ricevuto}': {testo}")

def start_subscriber(channel, ip_address):
    zmq_subscriber_thread = threading.Thread(target=__subscriber, args=(channel, ip_address))
    zmq_subscriber_thread.start()


def hello():
    print(f"Hi there {ZMQ_PORT}")