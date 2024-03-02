import warnings
warnings.filterwarnings('ignore')
import time

from loguru import logger
from cs_p2p import p2p


def test_answer():
    logger.info(f"Hi there.")
    p2p.hello()

    p2p.init()

    time.sleep(15)

    p2p.publish("zero", "Super!!!!!")

    assert 5 == 5