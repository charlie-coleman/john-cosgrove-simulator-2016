"""Launch point for John Cosgrove Simulator 2016."""
import setup
import functions
import sys
import time


def main():
    """Start bot in groupchat."""
    sys.stdout = open('log.txt', 'w')
    sys.stderr = open('log.txt', 'w')
    f = open('log.txt', 'w')
    chat_num = setup.TESTING_GROUND
    while setup.LOOP:
        f.truncate(0)
        print('THE TIME SINCE LAST MESSAGE WAS' + str(setup.TIME-time.time()) + ' SECONDS\n')
        functions.loop(setup.GROUP_IDS[chat_num], chat_num, setup.DELAY)


if __name__ == '__main__':
    main()
