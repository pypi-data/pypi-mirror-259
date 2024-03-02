import zmq
import time
import os
import queue
import threading

from dotenv import load_dotenv
from loguru import logger


load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
ZMQ_PORT_P= os.getenv("ZMQ_PORT_P")
MACHINE_IP = os.getenv("MACHINE_IP")
DEFAULT_IPS = os.getenv("DEFAULT_IPS")


class Publisher:

    def __init__(self) -> None:
        logger.info(f"Start Publisher")
        self.context = zmq.Context()
        # Create a PUB socket
        self.publisher = self.context.socket(zmq.PUB)
        self.publisher.bind(f"tcp://{MACHINE_IP}:{ZMQ_PORT_P}")
        self.zmq_queue = queue.Queue()
        self.node_id = 1

        self.zmq_publisher_thread = threading.Thread(target=self.__node_zmq_publisher)
        self.zmq_publisher_thread.start()

    def publish(self):
        topic = b'zero'
        message = b"Breaking news: Something important happened!"
        # Send the topic and message
        self.zmq_queue._put([topic, message])
        # self.publisher.send_string(message)
        # self.publisher.send_multipart([topic, message])
        logger.info(f"Message put in qeue...")

    def __node_zmq_publisher(self):
        while True:
            try:
                topic, message = self.zmq_queue.get(timeout=1)
                self.publisher.send_multipart([topic, message])
                logger.info(f"Message sent from the qeue...")
            except queue.Empty:
                pass
