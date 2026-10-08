import itertools
from colorama import Fore, Back, Style, init
init()

def win(current_game):

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            print(f'The Winner is player {l[0]}!')
            return True
        else:
            return False

    #normal diagonal winner
    diag_checker = []
    for num in range(len(game)):
        diag_checker.append(game[num][num])

    if all_same(diag_checker):
        return True

    #reverse diagonal winner
    rev_diag_checker = []
    for cols, rows in enumerate(reversed(range(len(game)))):
        rev_diag_checker.append(game[rows][cols])

    if all_same(rev_diag_checker):
        return True

    #vertical winner
    for col in range(len(game)):
        check = []

        for row in game:
            check.append(row[col])

        if all_same(check):
            return True

    #horizontal winner
    for row in game:
       if all_same(row):
            return True
    return False

def game_board(game_map, player = 0, row= 0, column= 0, just_display=False):
    try:
            if row < 0 or row >= len(game_map) or column < 0 or column >= len(game_map):
                    error_list = range(1, len(game_map))
                    print(f"Error: make sure you input row/column as {", ".join([str(i) for i in error_list])} or {len(game_map)}")
                    return game_map, False

            if game_map[row][column] != 0:
                print("This square is already occupied! Choose another :)")
                return game_map, False


            #Setting up the game board
            print("   " +"  ".join([str(i) for i in range(1, len(game_map) + 1)]))
            if not just_display:
                    game_map[row][column] = player


            for count, row in enumerate(game_map, start = 1):
                colored_row = ""
                for item in row:
                    if item == 0:
                        colored_row += "   "
                    elif item == 1:
                        colored_row += Fore.GREEN + ' X ' + Style.RESET_ALL
                    elif item == 2:
                        colored_row += Fore.MAGENTA + ' O ' + Style.RESET_ALL
                print(count, colored_row)

            return game_map, True

    except Exception as e:
        print("Something went very wrong!", e)
        return game_map, False

play = True
players = [1,2]
while play:
    game_size = int(input("What size game of tic tac toe? "))
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won = False
    game, _ = game_board(game, just_display=True)
    player_choice = itertools.cycle([1,2])
    while not game_won: 
        current_player = next(player_choice)
        print(f"Current Player is {current_player}")
        played = False
        
        while not played:
            options_list = range(1, game_size)

            try:
                column_choice = int(input(f"Which column would you like to play? {", ".join([str(i) for i in options_list])} or {game_size}?: "))
                row_choice = int(input(f"Which row would you like to play? {", ".join([str(i) for i in options_list])} or {game_size}?: "))
                game, played = game_board(game, current_player, row_choice - 1, column_choice - 1)

            except ValueError as e:
                print("Please enter a number!")
                

        if win(game):
            game_won = True
            again = input('Game is over, would you like to play again? (y/n)')
            if again.lower() == 'y':
                print('restarting')
            elif again.lower() == 'n':
                print('cya!')
                play = False
            else:
                print('not a valid answer, sooo cya!')
                play = False





