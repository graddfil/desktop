from configure import config, MatrixClient


def main():
    matrix = MatrixClient.from_config(config)
    matrix.send_message("Hello world!")

if __name__ == '__main__':
    main()
