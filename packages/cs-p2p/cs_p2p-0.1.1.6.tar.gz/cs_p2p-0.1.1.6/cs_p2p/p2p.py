import os
import queue
import zmq
import time
import threading

from dotenv import load_dotenv

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
SERVER_IP = os.getenv("SERVER_IP")
ROOT_IP = os.getenv("ROOT_IP")

def request_to_join():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    # Connettersi al nodo ricevente
    socket.connect(f"tcp://{ROOT_IP}:{ZMQ_PORT}")
    socket.send_string(SERVER_IP) 
    # Attendere la risposta
    response = socket.recv_string()
    print(f"Risposta dal Nodo {ROOT_IP}: {response}")
    # Chiudere il socket e il contesto
    socket.close()
    context.term()

def response_to_join():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    # Bind al socket su un indirizzo e una porta
    socket.bind(f"tcp://*:{ZMQ_PORT}")
    # Attendere la richiesta
    message = socket.recv_string()
    print(f"Ricevuta richiesta da: {message}")
    # Elaborare la richiesta (in questo caso, semplicemente rispondere)
    response = f"Ciao, sono il Nodo: {ROOT_IP}"
    socket.send_string(response)
    # Chiudere il socket e il contesto
    socket.close()
    context.term()





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