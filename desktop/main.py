import argparse
import confuse
from desktop.matrix import MatrixClient


def main():
    config = confuse.Configuration('graddfril')
    parser = argparse.ArgumentParser(description='Graddfril grabber aggregator')
    parser.add_argument('--clear-data', dest='wipe', action='store_true', default=False,
                        help='Reset data. (server, token, room)')
    args = parser.parse_args()


    matrix = MatrixClient.from_config(config, args)
    matrix.send_event("m.room.message", {"msgtype": "m.text",
                                         "body": "Hello world!"})
    matrix.send_event("graddfril.event", {"msgtype": "graddfril.keypress",
                                          "key": "h"})

if __name__ == '__main__':
    main()
