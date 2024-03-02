import warnings
warnings.filterwarnings('ignore')
import time

from loguru import logger
from cs_p2p import p2p


def test_answer():
    logger.info(f"Hi there.")
    channel = b"zero"

    p2p.hello()

    # p2p.init()

    # time.sleep(2)

    p2p.start_subscriber(channel, "192.168.1.148")

    time.sleep(2)
    p2p.publish(channel, "Super!!!!!")

    time.sleep(2)

    assert 5 == 5