if __package__ is None or __package__ == '':
    # uses current directory visibility
    from game.render_game import RanderGame
else:
    # uses current package visibility
    from .game.render_game import RanderGame


def start():
    print("\x1b[8;40;90t")  # This line is for resize user terminal
    game = RanderGame()
    game.play()


if __name__ == "__main__":
    start()
