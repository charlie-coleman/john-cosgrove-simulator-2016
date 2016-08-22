"""Initialization of John Cosgrove Simulator 2016."""
import pyphen
import configparser

pyphen.language_fallback('en_US')
dic = pyphen.Pyphen(lang='en_US')
config = configparser.ConfigParser()
config.read('.\\settings.ini')