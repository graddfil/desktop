import argparse
import confuse
from desktop.matrix import MatrixClient


def main():
    config = confuse.Configuration('graddfril')
    parser = argparse.ArgumentParser(description='Graddfril grabber aggregator')
    parser.add_argument('--wipe', action='store_true', help='Reset data. (server, token, room)')
    args = parser.parse_args()

    for name in ['server', 'room']:
        if name not in config or args.wipe:
            config[name].set(input('Please specify %s:' % name))
            open(config.user_config_path(), 'w').write(config.dump())

    if 'token' not in config or args.wipe:
        import getpass

        login_information = MatrixHttpApi(server).login("m.login.password",
                user=input("Please specify your username:"),
                password=getpass.getpass())
        if 'access_token' in login_information:
            config['token'].set(login_information['access_token'])
        else:
            raise NameError("Your password or login did't much.")

        # Save config.
        open(config.user_config_path(), 'w').write(config.dump())

    matrix = MatrixClient.from_config(config)
    matrix.send_event("m.room.message", {"msgtype": "m.text",
                                         "body": "Hello world!"})
    matrix.send_event("graddfril.event", {"msgtype": "graddfril.keypress",
                                          "key": "h"})

if __name__ == '__main__':
    main()
