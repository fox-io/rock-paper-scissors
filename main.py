"""
rock-paper-scissors
"""


def game():
    """
    Main game loop
    """
    print("rock-paper-scissors")

    while True:
        menu_command = input("""
        [P]lay
        [Q]uit
        """).lower()

        if menu_command == "p":
            # Play game
            print("playing game")
        elif menu_command == "q":
            # Quit game
            break
        else:
            print("Choose a menu option.")

    return


if __name__ == '__main__':
    game()
