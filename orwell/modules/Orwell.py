import socket
import ssl
import time
import json
from orwell.modules.Error import *
from orwell.modules.Logger import *


class Orwell:

    def __init__(self):
        self.logger = Logger()
        self.config = self.unpack_config()
        self.irc = socket.socket()
        self.is_connected = None

    def send(self, chan, msg):
        self.msg("PRIVMSG %s %s\n" % (chan, msg))

    def connect(self):
        try:
            server = self.config['server']
            channels = self.config['channels']
            port = self.config['port']
            nick = self.config['nick']
            password = self.config['password']

            self.logger.info("Opening new Orwell connection...")
            self.irc.connect((server, port))
            self.irc = ssl.wrap_socket(self.irc)
            self.on_connect(server, channels, nick, port, password)

        except SocketError as e:
            self.logger.warn(e("Connection disrupt in Orwell!"))
            raise e

    def on_connect(self, server, channels, nick, port, password):
        self.is_connected = True
        if password is not "":
            self.msg("PASS %s\n" % password)

        self.msg("USER %s %s %s :Orwell\n" % (nick, nick, nick)) # user authentication
        self.msg("NICK %s\n" % nick)
        time.sleep(2)

        for c in channels:
            self.msg("JOIN %s\n" % c)

    def disconnect(self):
        self.msg("QUIT Orwell rides her bike into the sunset...\n")
        self.logger.info("Closing Orwell connection...")
        self.irc.close()
        self.is_connected = False

    def msg(self, msg):
        self.irc.send(bytes(msg, 'utf-8'))

    def get_text(self):
        text = self.irc.recv(2048).decode('utf-8')  # receive the text

        if text.find('PING') != -1:
            self.msg('PONG %s\r\n' % text.split()[1])

        return text

    def unpack_config(self):
        try:
            with open('orwell/resources/orwell_config.json') as f:
                config = json.load(f)
            return config['irc']
        except FileError as e:
            self.logger.warn(e("Malformed Orwell JSON!"))
            raise e

