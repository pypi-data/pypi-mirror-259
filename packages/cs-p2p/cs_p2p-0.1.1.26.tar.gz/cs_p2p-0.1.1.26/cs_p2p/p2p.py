import os
import queue
import zmq
import time
import threading
import pickle
import subprocess

from dotenv import load_dotenv
from typing import List

# local imports
from cs_p2p.entity.Node import Node

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
MACHINE_IP = os.getenv("MACHINE_IP")
DEFAULT_IPS = os.getenv("DEFAULT_IPS")

def init():
    print("Starting process to connect to the Network...")
    nodes: List[Node] = []

    ip_addresses = DEFAULT_IPS.split(",")
    for ip_address in ip_addresses:
        # if ip_address != MACHINE_IP:
        # print(f"{ip_address} != {MACHINE_IP}")
        ip_address = ip_address.strip()

        new_node = Node(ip_address=ip_address)
        reputation = new_node.get_reputation(ip_address)
        new_node.reputation = reputation
        nodes.append(new_node)
    
    __save_nodes(nodes)
    __start_responder()
    print(f"Ciao")
    time.sleep(1)
    __request_to_join()
    
    
def __load_nodes() -> List[Node]:
    # load nodes data
    with open("nodes.pickle", "rb") as fp: 
        data = pickle.load(fp)
        nodes: List[Node] = data['nodes']
        
        # for node in nodes:
        #     print(f"node: {node.ip_address}")
    
    return nodes

def __save_nodes(nodes):
    with open("nodes.pickle", "wb") as fp: 
        data = {
            "nodes": nodes,
            "version":   "0.0.1",
            "timestamp":  time.time(),
        }
    
        pickle.dump(data, fp)

def __select_reputated_node():
    nodes: List[Node] = __load_nodes()
    best_node_ip = MACHINE_IP
    best_reputation = 0.0

    for node in nodes:
        if (node.reputation > best_reputation) and (node.ip_address != MACHINE_IP):
            best_node_ip = node.ip_address
            best_reputation = node.reputation

    return best_node_ip


def __request_to_join():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    # Connettersi al nodo ricevente
    best_node_ip = __select_reputated_node()

    print(f"best_node_ip: {best_node_ip}")

    socket.connect(f"tcp://{best_node_ip}:{ZMQ_PORT}")
    socket.send_string(MACHINE_IP) 
    # Attendere la risposta
    # response = socket.recv_string()
    # print(f"Risposta dal Nodo {best_node_ip}: {response}")

    nodes: List[Node] = socket.recv_pyobj()
    for node in nodes:
        print(f"nodo a cui sottoscriversi: {node.ip_address} -- {node.reputation}")
        start_subscriber("zero", node.ip_address)

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
        ip_address_requesgter = socket.recv_string()
        print(f"Ricevuta richiesta da: {ip_address_requesgter}. Mandare lista dei nodi a cui sottoscriversi")
        
        # Sottoscriversi a questo nodo

        # Publicare agli altri nodi di sottoscriversi a questo nodo

        # Mandare la lista dei nodi a cui questo nuovo nodo si deve sottoscrivere

       
        # response = f"Ciao, sono il Nodo: {MACHINE_IP}, ti mando la lista dei nodi a cui sottoscriverti"
        # socket.send_string(response)
        nodes: List[Node] = __load_nodes()
        socket.send_pyobj(nodes)

        # Chiudere il socket e il contesto
        # socket.close()
        # context.term()

def __start_responder():
    zmq_subscriber_thread = threading.Thread(target=__response_to_join)
    zmq_subscriber_thread.start()


def __publisher(channel, text):
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind(f"tcp://{MACHINE_IP}:{ZMQ_PORT}")
    
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
    print(f"Welcome to CS_P2P library.")



if __name__ == "__main__":
    init()