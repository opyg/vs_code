import random

tools = ['k', 'p', 'n']

def user_choice()->str:
    while True:
        user_input = input("Wybierz kamień('k') / papier('p') / nożyce('n') lub 'X' żeby skończyć grę: ")
        if user_input in tools or user_input == 'X':
            return user_input
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")

def computer_choice()->str:
    return random.choice(tools)

def game()->None:
    game_counter = 0
    win_counter = 0
    draw_counter = 0
    while True:
        user_tool = user_choice()
        if user_tool == 'X':
            print(f'GAME OVER\n Wyniki: Wygrałeś {win_counter} razy i zegrałeś w remis {draw_counter} razy na {game_counter} gry')
            break
        pc_tool = computer_choice()
        game_counter += 1
        if pc_tool == 'k' and user_tool == 'p' or pc_tool == 'p' and user_tool == 'n' or pc_tool == 'n' and user_tool == 'k':
            win_counter += 1
            print(f'Wygrałeś! {user_tool} pokonuje {pc_tool}')
        elif pc_tool == user_tool:
            draw_counter += 1
            print(f'Remis! {user_choice} = {pc_tool}')
        else:
            print(f'Przegrałeś! {pc_tool} pokonuje {user_tool}')

if __name__ == "__main__":
    game()

