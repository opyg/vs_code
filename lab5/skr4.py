import random

coin = ['o', 'r']

def coinflip_result()->str:
    return random.choice(coin)

def user_choice()->str:
    while True:
        user_input = input("Wybierz orzeł('o') lub reszka('r') lub 'X' żeby skończyć grę: ")
        if user_input in coin or user_input == 'X':
            return user_input
        else:
            print("Nieprawidłowy wybór! Spróbuj ponownie.")

def game()->None:
    game_counter = 0
    win_counter = 0
    while True:
        game_counter += 1
        user_coin = user_choice()
        if user_coin == 'X':
            print('GAME OVER')
            break    
        if coinflip_result() == user_coin:
            win_counter += 1
            print(f'Wygrałeś! Wygrałeś {win_counter} razy na {game_counter} gry')
        else:
            print(f'Przegrałeś! Wygrałeś {win_counter} razy na {game_counter} gry')
if __name__ == "__main__":
    game()