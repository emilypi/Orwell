from orwell.modules.Orwell import *
from orwell.modules.Error import *

def main():
    try:
        orwell = Orwell()
        orwell.connect()

        while orwell.is_connected:
            text = orwell.get_text()
            orwell.logger.info(text)

    except SocketError as e:
        orwell.logger.warn(e("Error with orwell connection!"))
        raise e

if __name__ == '__main__':
    main()