"""Functions for John Cosgrove Simulator 2016."""
import groupy
import setup
import time
import random


# Variables


name_phrases = ['My man!', 'I can say that \'cause he\'s not here!',
                'What\'s the good word?', 'Can I getcha a pretzel?']
johnisms = ['What\'s the good word?', 'Can I getcha a pretzel?', '*Turns off all the electronics in the room at 8pm*',
            '*Rolls around in bed when Payton turns on his iPad*', '*Eats chicken tenders*',
            '*Identifies plane overhead*', 'Ahhh, shooting the ILS approach into Schafer.',
            '*Sits at clocktower for 48 hours straight*', '*Dons windbreaker*',
            '*Sees somebody in his chair, has nervous breakdown*']
trigger_names = ['jimmy garrity', 'tristan davies']
output_names = ['Hah-mez Guh-rrity', 'Trist-in Duh-veez']
hold_message = None
check_user = None
check_message = None
time_last_sent = 0

# Setup Functions


def get_bot(bot_index):
    """Returns the bot by index."""
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
    """Determine if message contains command, if so, triggers command. Also triggers check_names"""
    if not message:
        message = 'NULL AND VOID'
    message_arr = message.split()
    if message_arr[0] in commands:
        command_functions[commands.index(message_arr[0])](message, bot)
    elif message_arr[0] in admin_commands:
        admin_functions[admin_commands.index(message_arr[0])](message, bot)
    check_names(message, bot)


def check_names(message, bot):
    """Determines if a trigger name is in the message, if so, outputs modified name and a quote by John."""
    for name in trigger_names:
        if name in message.lower():
            bot.post(output_names[trigger_names.index(name)]+'! '+random.choice(name_phrases))


def loop(group_id, bot_index, delay):
    """Main loop."""
    bot = get_bot(bot_index)
    group = get_group(group_id)
    message = get_most_recent_message(group)
    if message.user_id in setup.ADMINS:
        setup.ADMIN = True
    else:
        setup.ADMIN = False
    prevent_disconnect(message, bot)
    parse_message(message.text, bot)
    time.sleep(delay)


def check_elapsed_time():
    """Check time passed since last message."""
    elapsed_time = time.time() - setup.TIME
    return elapsed_time


def update_time(message):
    """Update time """
    global hold_message
    if hold_message != message.text:
        setup.TIME = time.time()
        hold_message = message.text


def prevent_disconnect(message, bot):
    """Checks to make sure it doesn't respond to the same message twice"""
    global check_message, time_last_sent
    if check_message != message.created_at:
        check_message = message.created_at
        time_last_sent = time.time()
    if time.time()-time_last_sent > 4400:
        johnism(message, bot)


# Regular Commands


def check_and_multiply_letters(syllable, letter_list, x, *backup_list):
    """Multiplies every letter in syllables found in letter_list x times."""
    for letter in syllable[:-1]:
        if letter in letter_list:
            syllable = syllable.replace(letter, letter+''.join([letter.lower() for s in range(x-1)]), 1)
            return syllable
    if len(backup_list) > 0:
        check_and_multiply_letters(syllable, backup_list, x)
    return syllable


def johnify(message, bot):
    """Rewrite words as they would be pronounced by John Cosgrove."""
    words = message.split()[1:]
    for i in range(len(words)):
        syllables = setup.DICT.inserted(words[i]).split('-')
        for j in range(0, len(syllables), 2):
            syllables[j] = check_and_multiply_letters(syllables[j], setup.VOWELS, 4, 'yY')
            print(syllables[j])
        words[i] = ''.join(syllables)
    output_string = ' '.join(words) + '!'
    bot.post(output_string)


def johnism(message, bot):
    """Print out a Johnism."""
    output_string = random.choice(johnisms)
    bot.post(output_string)


# Admin Commands


def disconnect(message, bot):
    """Disconnect the bot."""
    setup.LOOP = False
    bot.post('Welp, off to bed. Got a long day tomorrow! *Is 9:45PM*')


# Command Setup


commands = ['!johnify', '!johnism']
command_functions = [johnify, johnism]
admin_commands = ['!disconnect']
admin_functions = [disconnect]
