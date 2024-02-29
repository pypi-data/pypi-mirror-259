import os

from dotenv import load_dotenv

load_dotenv()

ZMQ_PORT= os.getenv("ZMQ_PORT")

def hello():
    print(f"Hi there {ZMQ_PORT}")


if __name__ == "__main__":
    hello()
    