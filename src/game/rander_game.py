from src.game.baboo_game import BabooGame
from src.lib.abstract_dice import *
import src.config.color_config as color
from src.config.text_constant import *


class RanderGame:
    def __init__(self):
        print(self.__show_text(WELCOME_MESSAGE, color.YELLOW))
        print(self.__show_text(DICE_IMAGE, color.BLUE))
        self.__player_name = self.__get_player_name()
        self.__board = Dice(D4, D4, D4, D4, D8, D6)
        self.__game = BabooGame(self.__board, self.__player_name)
        self.__round = 1

    def __get_player_name(self):
        # name = input(self.__show_text("Please insert your name: "))
        name = "STRANGER"
        return name

    def __show_text(self, text, col=color.WHITE):
        return f"{col}{text}{color.RESET}"


    def __show_menu(self):
        print(self.__show_text("""
1. Continue     2. Roll specific dice     3. Add new die    4. Withdraw
        """))


    def __display_board(self):
        dice_list = self.__game.dice

        print(self.__show_text(f"{'▔' * 50}{'▔▔▔▔▔▔▔▔▔▔▔▔▔' * (len(dice_list) - 4)}"))
        print(self.__show_text("Round:"), self.__show_text(self.__round, color.GREEN), end="    ")

        status_lose = self.__show_text("Lose", color.RED)
        status_win = self.__show_text("Win", color.GREEN)

        if self.__game.check_winner():
            print(self.__show_text("Status:"), status_win, end="     ")
        else:
            print(self.__show_text("Status:"), status_lose, end="     ")

        print(self.__show_text(f"Balance: {self.__game.credit_balance}"), end="     ")
        print(end="\n\n")

        for die in dice_list:
            print("    ", self.__show_text(die.face, color.Fore.LIGHTCYAN_EX), end="       ")
        print()

        for line in range(5):
            for die in dice_list:
                print(self.__show_text(DICE.get(die.face)[line], color.BLUE), end="  ")
            print()

        for die in dice_list:
            print("    ", self.__show_text(type(die).__name__, color.MAGENTA), end="      ")
        print(end="\n")

        print(self.__show_text(f"{'▁' * 50}{'▁▁▁▁▁▁▁▁▁▁▁▁▁' * (len(dice_list) - 4)}"))
        self.__show_menu()

    def play(self):
        # input("Press ENTER to start the game: ")
        print(self.__show_text(START_GAME, color.RED))
        self.__display_board()
        print(self.__show_text(GAME_OVER, color.RED))
