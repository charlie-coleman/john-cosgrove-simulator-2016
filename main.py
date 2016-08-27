"""Launch point for John Cosgrove Simulator 2016."""
import setup
import functions
import sys
import time


def main():
    """Start bot in groupchat."""
    chat_num = setup.NEW_IMPROVED
    while setup.LOOP:
        functions.loop(setup.GROUP_IDS[chat_num], chat_num, setup.DELAY)


if __name__ == '__main__':
    main()
