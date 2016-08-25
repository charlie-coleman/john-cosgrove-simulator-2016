"""Launch point for John Cosgrove Simulator 2016."""
import setup
import functions


def main():
    """Start bot in groupchat."""
    chat_num = setup.TESTING_GROUND
    bot = functions.get_bot(chat_num)
    while setup.LOOP:
        functions.loop(setup.GROUP_IDS[chat_num], bot, setup.DELAY)

if __name__ == '__main__':
    main()
