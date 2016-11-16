from orwell_irc import *
from threading import Thread
import time

channel = "#wetfish"
server = "irc.wetfish.net"
nick = "Orwell"
port = 6697
password = "f8067b8daf5d1b2467b2d448858794468d451232b3de4a0f6262c2ec733acf24"

def loop():

    orwell = Orwell()
    orwell.connect(server, channel, nick, port, password)

    while True:
        try:
            text = orwell.get_text()
            print(text)

            if "PRIVMSG" in text and channel in text and "hello" in text:
                orwell.send(channel, bytes("Hello, emilypi :)", 'utf-8'))
        except socket.error as e:
            if str(e) == "[Errno 35] Resource temporarily unavailable":
                time.sleep(0)
                continue
            raise e

        finally:
            orwell.disconnect()

def main():
    t = Thread(target=loop)
    t.daemon = True
    t.start()

if __name__ == '__main__':
    main()