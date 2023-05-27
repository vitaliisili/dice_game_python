from src.game.rander_game import RanderGame

if __name__ == "__main__":
    print("\x1b[8;40;90t")  # This line is for resize user terminal
    game = RanderGame()
    game.play()


