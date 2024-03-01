import os
import queue
import zmq
import time
import threading
import pickle
import subprocess

from dotenv import load_dotenv

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
SERVER_IP = os.getenv("SERVER_IP")
ROOT_IP = os.getenv("ROOT_IP")
DEFAULT_IPS = os.getenv("DEFAULT_IPS")

def init():
    print("Init node...")
    nodes = []

    ip_addresses = DEFAULT_IPS.split(",")
    for ip_address in ip_addresses:
        ip_address = ip_address.strip()
        reputation = __ping_ip(ip_address)
        
        node = {
            "ip_address" : ip_address,
            "reputation" : reputation
        }

        nodes.append(node)
    
    __save_nodes(nodes)
    __start_responder()

    
def __load_nodes():
    # load nodes data
    with open("nodes.pickle", "rb") as fp: 
        data = pickle.load(fp)
    
    nodes = data["nodes"]
    return nodes


def __save_nodes(nodes):
    with open("nodes.pickle", "wb") as fp: 
        data = {
            "nodes": nodes,
            "version":   "0.0.1",
            "timestamp":  time.time(),
        }
    
        pickle.dump(data, fp)


def __ping_ip(ip_address, count=3):
    # Costruisci il comando di ping
    command = ['ping', '-c', str(count), ip_address]
    counter = 0
    reputation = 1

    try:
        # Esegui il comando e cattura l'output riga per riga
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        for line in process.stdout:
            counter +=1
            # print(f"{counter}: {line.strip()}")
            if counter == 7:
                elements = line.strip().split(",")
                value = elements[2].strip().split(" ")[0]
                value = float(value[:-1])
                print(f"value: {value}")
                if value == 0.0:
                    reputation = 100

        # Attendere che il processo termini
        process.wait()

        # Verifica se ci sono errori nel processo
        # if process.returncode != 0:
        #     print(f"Errore durante il ping. Codice di ritorno: {process.returncode}")
    except subprocess.CalledProcessError as e:
        # Se c'è un errore, stampa l'errore
        print(f"Errore durante il ping: {e}")
    
    return reputation

def __select_reputated_node():
    nodes = __load_nodes()
    best_node_ip = SERVER_IP
    best_reputation = 0.0

    for node in nodes:
        ip_address = node['ip_address']
        reputation = float(node['reputation'])

        if reputation > best_reputation:
            best_node_ip = ip_address
            best_reputation = reputation

    print(best_node_ip)
    print(best_reputation)
    return best_node_ip


def request_to_join():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    # Connettersi al nodo ricevente
    best_node_ip = __select_reputated_node()
    socket.connect(f"tcp://{best_node_ip}:{ZMQ_PORT}")
    socket.send_string(SERVER_IP) 
    # Attendere la risposta
    response = socket.recv_string()
    print(f"Risposta dal Nodo {best_node_ip}: {response}")
    # Chiudere il socket e il contesto
    socket.close()
    context.term()

def __response_to_join():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    # Bind al socket su un indirizzo e una porta
    socket.bind(f"tcp://*:{ZMQ_PORT}")

    while True:
        # Attendere la richiesta
        message = socket.recv_string()
        print(f"Ricevuta richiesta da: {message}")
        # Elaborare la richiesta (in questo caso, semplicemente rispondere)
        response = f"Ciao, sono il Nodo: {SERVER_IP}"
        socket.send_string(response)
        # Chiudere il socket e il contesto
        # socket.close()
        # context.term()

def __start_responder():
    zmq_subscriber_thread = threading.Thread(target=__response_to_join)
    zmq_subscriber_thread.start()


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



if __name__ == "__main__":
    init()