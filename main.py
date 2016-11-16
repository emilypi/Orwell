from orwell import *
from threading import Thread
import time
import logging
from logging.config import fileConfig

channel = "#wetfish"
server = "irc.wetfish.net"
nick = "Orwell"
port = 6697
password = ""

def loop():

    orwell = Orwell()
    orwell.connect(server, channel, nick, port, password)

    while orwell.connected:
        try:
            text = orwell.get_text()
            print(text)

            if "PRIVMSG" in text in text and "please quit" in text and "emilypi" in text:
                orwell.disconnect()

            if "KICK" in text and channel in text and "Orwell" in text:
                time.sleep(5)
                orwell.msg("JOIN %s\n" % channel)

        except socket.error as e:
            raise e

        logging.info("All cleaned up!")

def main():
    fileConfig('resources/logging_config.ini')
    logger = logging.getLogger(__name__)
    logger.info('Started Orwell...')

    loop()

if __name__ == '__main__':
    main()