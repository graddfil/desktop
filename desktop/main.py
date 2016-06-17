from matrix_client.api import MatrixHttpApi
from matrix_client.api import MatrixRequestError
import confuse
import argparse

config = confuse.Configuration('graddfil')
parser = argparse.ArgumentParser(description='Graddfil desktop app')
parser.add_argument('--logout', dest='logout', action='store_true', default=False,
                    help='Logout from current user')

server_url = "https://matrix.org"  # without '/'

def get_token(username, password):
    'Get Matrix token by user and password'
    login_information = MatrixHttpApi(server_url).login("m.login.password",
                    user=username, password=password)
    if 'access_token' in login_information:
        return login_information['access_token']
    else:
        raise NameError('Your password or login did\'t mutch')

def login():
    '''
    Login user with token if there\s no token get username and password.
    Will return MatrixHttpApi
    '''

    # Check for token
    if 'token' not in config or parser.parse_args().logout:
        import getpass
        username = input('Please specify your username:')
        password = getpass.getpass()

        try:
            # Set token and save config
            config['token'].set(get_token(username, password))
            open(config.user_config_path(), 'w').write(config.dump())
        except MatrixRequestError:
            print('Your password or username didn\'t match, please try again.')
            login()
    return MatrixHttpApi(server_url, token=config['token'].get())

def main():
    matrix = login()
    response = matrix.send_message("!dppXJSqykoVCKXEPcO:matrix.org", "Hello from python SDK!")

if __name__ == '__main__':
    main()
