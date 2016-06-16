from matrix_client.api import MatrixHttpApi
from matrix_client.api import MatrixRequestError
import confuse
import argparse

server_url = "https://matrix.org"  # without '/'

def get_token(username, password):
    'Get Matrix token by user and password'
    login_information = MatrixHttpApi(server_url).login("m.login.password",
                    user=username, password=password)
    if 'access_token' in login_information:
        return login_information['access_token']
    else:
        raise NameError('Your password or login did\'t mutch')


def main():
    parser = argparse.ArgumentParser(description='Graddfil desktop app')

    # We need to logout user
    parser.add_argument('--logout', dest='logout', action='store_true', default=False,
                                            help='Logout from current user')

    config = confuse.Configuration('graddfil-desktop')

    if 'token' not in config or parser.parse_args()['logout']:
        import getpass
        username = input('Please specify your username:')
        password = getpass.getpass()

        try:
            config['token'].set(get_token(username, password))
        except MatrixRequestError:
            print('Your password or username didn\'t match')
            main()
            return

    matrix = MatrixHttpApi(server_url, token=config['token'].get())
    response = matrix.send_message("!dppXJSqykoVCKXEPcO:matrix.org", "Hello from python SDK!")
    config.dump(redact=True)

if __name__ == '__main__':
        main()
