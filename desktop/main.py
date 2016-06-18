from configure import config, MatrixClient


def main():
    matrix = MatrixClient.from_config(config)
    matrix.send_event("m.room.message", {"msgtype": "m.text",
                                         "body": "Hello world!"})
    matrix.send_event("graddfril.event", {"msgtype": "graddfril.keypress",
                                          "key": "h"})

if __name__ == '__main__':
    main()
