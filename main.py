"""Main module for John Cosgrove Simulator 2016."""
import groupy
from setup import *
from functions import *


def main():
    """Start bot in groupchat."""
    bot = get_bot(NEW_IMPROVED)
    while True:
        loop(GROUP_IDS[NEW_IMPROVED], bot, DELAY)

if __name__ == '__main__':
    main()
