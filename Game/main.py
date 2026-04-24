from play_game import play_game

def game_menu():
    while True:
        print("\n---- GAME MENU ----")
        print("1. Play Game")
        print("2. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            play_game()
        elif choice == "2":
            print("Game Over")
            break
        else:
            print("Invalid choice")
game_menu()