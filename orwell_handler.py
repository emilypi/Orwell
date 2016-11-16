from orwell_irc import *
from threading import Thread
import time

channel = "#wetfish"
server = "irc.wetfish.net"
nick = "Orwell"
port = 6697
password = ""

def loop():

    orwell = Orwell()
    orwell.connect(server, channel, nick, port, password)

    while True:
        try:
            text = orwell.get_text()
            print(text)

            if "PRIVMSG" in text in text and "please quit" in text and "emilypi" in text:
                orwell.disconnect()

            if "KICK" in text and channel in text and "Orwell" in text:
                time.sleep(5)
                orwell.msg("JOIN %s\n" % channel)


        except socket.error as e:
            if str(e) == "[Errno 35] Resource temporarily unavailable":
                time.sleep(0)
                continue

            raise e

    orwell.disconnect()
    return

def main():
    loop()

if __name__ == '__main__':
    main()