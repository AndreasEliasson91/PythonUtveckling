from game.game import Game

HOST = '127.0.0.1'
PORT = 32198


def main():
    game = Game(HOST, PORT)
    game.run()


if __name__ == '__main__':
    main()
