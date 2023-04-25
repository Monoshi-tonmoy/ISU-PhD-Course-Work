#I have implemented this to let two AI agents play with varying heuristic functions and depth, by running this module, I will try to answer question number 5 and 6.


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
        #move,time_2 = Othello.agent2_move(game,depth_2)  #When I was considering two different evaluation functions
        move,time_2=Othello.agent1_move_W(game,depth_2)
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


File=open("OutputFor6.txt","a") 

File.write("Agent 1 is black and Agent 2 is white.....\n")
File.write("Playing using same evaluaiton funciton (Weighted position) with different depth values\n")
File.write("Depth for agent 1 is "+str(depth_1)+" and "+str(depth_2)+" for agent 2\n\n")
File.write("Here is your winner..............................................\n")

if(winner=='B'):
    File.write("The winner is agent 1, depth "+str(depth_1)+"\n")
else:
    File.write("The winner is agent 2, depth "+str(depth_2)+"\n")

File.write("Agent 1 takes "+str(agent_1)+" seconds and agent 2 takes "+str(agent_2)+" seconds\n")
File.write("\n\n\n\n\n\n\n\n\n\n\n")
