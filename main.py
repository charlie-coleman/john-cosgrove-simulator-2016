"""Launch point for John Cosgrove Simulator 2016."""
import setup
import functions


def main():
    """Start bot in groupchat."""
    chat_num = setup.TESTING_GROUND
    while setup.LOOP:
        functions.loop(setup.GROUP_IDS[chat_num], chat_num, setup.DELAY)


if __name__ == '__main__':
    main()
