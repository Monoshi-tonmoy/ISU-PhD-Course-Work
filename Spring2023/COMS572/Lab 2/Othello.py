from games import Othello

def main():
    game = Othello()
    print("..............Here is the initial formation of the board....................") #B for Black and W for white
    print("Human is playing color Black and Agent is playing color White")
    while not game.is_game_over():
        game.print_board()
        if game.current_player == 'B':
            move, taken_time = Othello.human_move(game)
            print()
            print("Suggesgted Move for you using Alpha-Beta cutoff Search: ({}, {})".format(move[0], move[1]))
            print("However your all available valid moves are:",game.get_valid_moves(game.current_player))
            row, col = input("Enter your move selecting any of the available moves (comma-separated): ").split(',')
            row, col = int(row), int(col)
            if game.is_valid_move(row, col, game.current_player):
                game.make_move(row, col, game.current_player)
            else:
                print("Please enter a valid move! You have already got all valid moves!")
        else:
            print()
            print("Your opponent is thinking!!!!")
            move, taken_time_2 = Othello.agent_move(game)
            if move is not None:
                print("Agent chooses: ({}, {})".format(move[0], move[1]))
                game.make_move(move[0], move[1], game.current_player)
            else:
                print("Agent has no valid moves.")

    print("Game Over!!!!!\nGuess who has won this game?")
    winner = game.get_winner()
    if winner == 'Tie':
        print("The game is a tie.")
    elif winner=='B':
        print("Congratulations human player, you have won the match...\n")
    else:
        print("Sorry, you lose, please try again.\n")



if __name__ == "__main__":
    main()