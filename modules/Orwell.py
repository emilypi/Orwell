from modules.Logger import *
import socket
import ssl
import time


class Orwell:

    def __init__(self):
        self.logger = Logger()

        self.logger.info("Starting up new Orwell instance...")

        self.irc = socket.socket()
        self.connected = None

    def send(self, chan, msg):
        self.msg("PRIVMSG %s %s\n" % (chan, msg))

    def connect(self, server, channel, nick, port, password):
        self.logger.info("Connecting to:\t%s\n" % server)

        self.irc.connect((server, port))
        self.irc = ssl.wrap_socket(self.irc)
        self.on_connect(server, channel, nick, port, password)

        self.logger.info("Successful connection!\n")

    def on_connect(self, server, channel, nick, port, password):
        self.connected = True
        if password is not "":
            self.msg("PASS %s\n" % password)

        self.msg("USER %s %s %s :Orwell\n" % (nick, nick, nick)) # user authentication
        self.msg("NICK %s\n" % nick)

        time.sleep(2)
        self.msg("JOIN %s\n" % channel)

    def disconnect(self):
        self.msg("QUIT Orwell rides her bike into the sunset...\n")
        self.irc.detach()
        self.irc.close()
        self.connected = False

        self.logger.info("Closing Orwell connection...")

    def msg(self, msg):
        self.irc.send(bytes(msg, 'utf-8'))

    def get_text(self):
        text = self.irc.recv(2048).decode('utf-8')  # receive the text

        if text.find('PING') != -1:
            self.msg('PONG %s\r\n' % text.split()[1])

        return text
