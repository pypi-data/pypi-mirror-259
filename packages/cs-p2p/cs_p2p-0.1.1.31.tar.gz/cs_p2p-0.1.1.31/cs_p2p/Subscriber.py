import zmq
import time
import os
import queue

from dotenv import load_dotenv
from loguru import logger

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")
ZMQ_PORT_P= os.getenv("ZMQ_PORT_P")

class Subscriber:

    def __init__(self, ip_address, zmq_queue) -> None:
        logger.info(f"Start Subscriber")
        self.context = zmq.Context()
        # Create a PUB socket
        self.subscriber = self.context.socket(zmq.SUB)
        self.subscriber.connect(f"tcp://{ip_address}:{ZMQ_PORT_P}")
        # Subscribe to the "News" topic
        self.subscriber.setsockopt(zmq.SUBSCRIBE, b'zero')
        self.zmq_queue = zmq_queue

    def run(self):
        while True:
            time.sleep(2)
            [topic, message] = self.subscriber.recv_multipart()
            logger.warning(f"Received: {topic.decode()} - {message.decode()}")
            
            #do the computation part!
            new_message = b"Do some calculus"
            self.zmq_queue._put([topic, new_message])
            logger.info(f"Message put in qeue...")