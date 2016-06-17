from matrix_client.api import MatrixHttpApi
from matrix_client.api import MatrixRequestError
import confuse
import argparse

config = confuse.Configuration('graddfil')
parser = argparse.ArgumentParser(description='Graddfil desktop app')
parser.add_argument('--clear-data', dest='wipe', action='store_true', default=False,
                    help='Reset data. (server, token, room)')


class Graddfril:
    '''
    :param token: Matrix token.
    :param server: Matrix server to use.
    :param room: Room id for sending data.
    '''

    def __init__(self):
        '''
        We need to check configuration file.
        If room, host, token not in configuration file we ask to input them.
        '''

        for name in ['server', 'room']:
            if name not in config or parser.parse_args().wipe:
                config[name].set(input('Please specify %s:' % name))
                open(config.user_config_path(), 'w').write(config.dump())
        self.server = config['server'].get()
        self.room = config['room'].get()

        if 'token' not in config or parser.parse_args().wipe:
            import getpass
            try:

                login_information = MatrixHttpApi(self.server).login("m.login.password",
                                                                     user=input("Please specify your username:"),
                                                                     password=getpass.getpass())
                if 'access_token' in login_information:
                    config['token'].set(login_information['access_token'])
                else:
                    raise NameError("Your password or login did't much.")

                # Save config.
                open(config.user_config_path(), 'w').write(config.dump())
            except MatrixRequestError:
                print("Your password or username didn't match, please try again.")

        self.token = config['token'].get()

    def send_message(self, data):
        print(MatrixHttpApi(self.server, token=self.token).send_message(self.room, data))
