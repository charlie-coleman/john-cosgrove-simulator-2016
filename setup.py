"""Initialization of John Cosgrove Simulator 2016."""
import pyphen
import configparser
import time
import os
# Setup hyphenator and other global variables


pyphen.language_fallback('en_US')
DICT = pyphen.Pyphen(lang='en_US')
config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), 'settings.ini'))
LOOP = True
ADMIN = False
PREVENT_DISCONNECT = False
TIME = time.time()


# Read the .ini file


ADMINS = config.get('Setup', 'Admins').split(',')
GROUP_IDS = config.get('Setup', 'GroupIDs').split(',')
NEW_IMPROVED = 0
TESTING_GROUND = 1
THREE_C = 2
LANGUAGE = config.get('Setup', 'Language')
DELAY = config.getint('Setup', 'Delay')/1000.0
TIMEOUT_TIME = config.getint('Setup', 'Timeout')
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'y', 'Y')
