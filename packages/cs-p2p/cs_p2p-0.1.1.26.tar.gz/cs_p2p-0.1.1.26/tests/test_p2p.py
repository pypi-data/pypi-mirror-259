import warnings
warnings.filterwarnings('ignore')

from loguru import logger
from cs_p2p import p2p


def test_answer():
    logger.info(f"Hi there.")
    p2p.hello()

    p2p.init()


    assert 5 == 5