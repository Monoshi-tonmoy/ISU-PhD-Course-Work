#Comparing two varing heuristics


from games import Othello

game = Othello()
agent_1=0
agent_2=0
depth_1=int(input("Enter depth value for first agent: "))
depth_2=int(input("Enter depth value for second agent: "))

while not game.is_game_over():
    game.print_board()
    if game.current_player == 'B':
        move,time_1 = Othello.agent1_move(game,depth_1)
        agent_1+=time_1
        if move is not None:
            print("First agent chooses: ({}, {})".format(move[0], move[1]))
            game.make_move(move[0], move[1], game.current_player)
        else:
            print("First agent has no valid moves.")
    else:
        move,time_2 = Othello.agent2_move(game,depth_2) 
        agent_2+=time_2
        if move is not None:
            print("Second agent chooses: ({}, {})".format(move[0], move[1]))
            game.make_move(move[0], move[1], game.current_player)
        else:
            print("Second agent has no valid moves.")

print("Agent1 takes ",agent_1," Agent2 takes", agent_2)
print("\n\n")
print("Game over!")
winner = game.get_winner()
if winner == 'Tie':
    print("Draw Game!")
else:
    print("The winner is player", winner)


File=open("OutputFor7.txt","a") 

File.write("Agent 1 is black and Agent 2 is white.....\n")
File.write("One evaluation function: Weighted position (Agent 1) and another one: normal counting and substraction of white and black pieces(Agent 2).\n")
File.write("Depth for agent 1 is "+str(depth_1)+" and "+str(depth_2)+" for agent 2\n\n")
File.write("Here is your winner..............................................\n")

if(winner=='B'):
    File.write("The winner is agent 1 with weighted position evaluation funciton, depth "+str(depth_1)+"\n\n")
else:
    File.write("The winner is agent 2 with normal evaluation funciton, depth "+str(depth_1)+"\n\n")

File.write("\n\n\n\n\n\n\n\n\n")