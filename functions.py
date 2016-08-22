"""Functions for John Cosgrove Simulator 2016."""
import groupy
import setup
import time


def get_bot(bot_index):
    return groupy.Bot.list()[bot_index]


def get_group(group_id):
    """Get Group By ID."""
    group = None
    for inc_group in groupy.Group.list():
        if inc_group.group_id == group_id:
            group = inc_group
    return group


def get_most_recent_message(group):
    """Return the most recently sent message."""
    messages = group.messages()
    return messages.newest


def parse_message(message, bot):
    """Determine if message contains command, if so, triggers command."""
    message_arr = message.split()
    if message_arr[0] in commands:
        command_functions[commands.index(message_arr[0])](message, bot)


def loop(group_id, bot, delay):
    """Main Loop."""
    group = get_group(group_id)
    message = get_most_recent_message(group)
    parse_message(message.text, bot)
    time.sleep(delay)


def johnify(message, bot):
    """Rewrite words as they would be pronounced by John Cosgrove."""
    words = message.split()[1:]
    for i in range(len(words)):
        syllables = setup.DICT.inserted(words[i]).split('-')
        replaced = False
        for letter in syllables[0][:-1]:
            if letter in setup.VOWELS and not replaced:
                syllables[0] = syllables[0].replace(letter, letter+''.join([letter.lower() for s in range(3)]))
                replaced = True
        if not replaced:
            for letter in syllables[0][:-1]:
                if letter in 'yY' and not replaced:
                    syllables[0] = syllables[0].replace(letter, letter+''.join([letter.lower() for s in range(3)]))
                    replaced = True
        words[i] = ''.join(syllables)
    output_string = ' '.join(words)
    output_string += '!'
    bot.post(output_string)

commands = ['!johnify']
command_functions = [johnify]
