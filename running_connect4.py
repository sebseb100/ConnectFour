import connectfour as lib
import cf_library as shell

def game():
    '''
    Phew here we are
    The following function utilizes the connectfour library provided by Professor Thorton
    As well as the connectfour_shell that is the additional logic of the game library
    In order to actually execute the shell version of the game
    '''
    print("Connect 4. Let the games begin.")

    #PROMPT USER FOR SIZE OF BOARD
    
    columns,rows =  shell.how_many_rows_columns()

    #WE'RE GOOD UP TO HERE THE PROGRAM TAKES IN THE COLUMNS AND ROWS AND ADDS IT TO THE NAMEDTUPLE
    current_game = lib.new_game(columns,rows)

    #While the game is not over lib.winner() references the provided function if winner doesn't determine a winner it returns the EMPTY value which is 0
    #This must remain true for the game to continue to be played
    
    while lib.winner(current_game) == lib.EMPTY:

        shell.display_game_board(current_game,rows,columns)

        shell.turn(current_game)

        while True:

            column, move = shell.get_move(columns)

            try:

                current_game = shell.player_move(current_game, column, move)

                break 

            except lib.InvalidMoveError:

                if move == shell.POP:
                    print("You can not pop the selected column.")
                elif move == shell.DROP:
                    print("You can not drop a peice into the selected column.")

    shell.display_game_board(current_game,rows,columns)

    print(f'{shell.red_or_yellow(lib.winner(current_game))} has won the game.')  
    return None
    
if __name__ == '__main__':
    game()
