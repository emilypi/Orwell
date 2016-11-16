from modules.Orwell import *
from modules.Logger import *

channel = "#bots"
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


def main():
    loop()

if __name__ == '__main__':
    main()