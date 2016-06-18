from matrix_client.api import MatrixHttpApi
import confuse
import argparse

config = confuse.Configuration('graddfil')
parser = argparse.ArgumentParser(description='Graddfil desktop app')
parser.add_argument('--clear-data', dest='wipe', action='store_true', default=False,
                    help='Reset data. (server, token, room)')
args = parser.parse_args()


class MatrixClient:
    '''
    :param server: Matrix server to use.
    :param token: Matrix token.
    :param room: Room id for sending data.
    '''

    def __init__(self, server: str, token: str, room: str):
        self.server = server
        self.token = token
        self.room = room
        self.api = MatrixHttpApi(self.server, token=self.token)


    @classmethod
    def from_config(cls, config: confuse.Configuration):
        '''
        We need to check configuration file.
        If room, host, token not in configuration file we ask to input them.
        '''

        for name in ['server', 'room']:
            if name not in config or args.wipe:
                config[name].set(input('Please specify %s:' % name))
                open(config.user_config_path(), 'w').write(config.dump())
        server = config['server'].get()
        room = config['room'].get()

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

        token = config['token'].get()

        return cls(server, token, room)

    def send_message(self, data):
        return self.api.send_message(self.room, data)
