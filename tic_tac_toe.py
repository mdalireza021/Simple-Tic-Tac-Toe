import time
import os

def Score_Board(score_board):
    print("\n\n\n\t--------------------------------------")
    print("\t              SCOREBOARD              ")
    print("\t--------------------------------------")
    players = list(score_board.keys())
    print(" \tPlayer 1 [X]\t", players[0], "\t", score_board[players[0]])
    print(" \tPlayer 2 [O]\t", players[1], "\t", score_board[players[1]])

    print("\t------------------------------------\n")

def Draw_Box(values):
    print("\n\t\t     |     |")
    print("\t\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t\t_____|_____|_____')

    print("\t\t     |     |")
    print("\t\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t\t_____|_____|_____')

    print("\t\t     |     |")

    print("\t\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t\t     |     |\n")


def Check_Win(player_pos, cur_player):

    value_all = [[1, 2, 3], [1, 4, 7], [1, 5, 9], [3, 5, 7], [3, 6, 9], [4, 5, 6], [7, 8, 9], [2, 5, 8]]
    for x in value_all:
        if all(y in player_pos[cur_player] for y in x):
            return True
    return False

def Check_Draw(player_pos):
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return True
    return False



def Play_Game(cur_player):
    values = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player_pos = {'X': [], 'O': []}
    while True:
        os.system('cls')
        Score_Board(score_board)
        Draw_Box(values)
        try:
            print("\t",cur_player, " turn.Enter the position between[1-9]: ")
            move = int(input())
        except ValueError:
            print("Wrong Input! Try Again")
            time.sleep(1)
            continue

        if move < 1 or move > 9:
            print("Wrong Input!Try Again")
            time.sleep(1)
            continue

        if values[move - 1] != ' ':
            print("Place already filled. Try again!!")
            time.sleep(2)
            continue
        values[move - 1] = cur_player
        player_pos[cur_player].append(move)
        if Check_Win(player_pos, cur_player):
            Draw_Box(values)
            print("Player ", cur_player, " has won the game!!")
            print("\n")
            time.sleep(3)
            return cur_player
        if Check_Draw(player_pos):
            Draw_Box(values)
            print("Game Drawn")
            print("\n")
            time.sleep(3)
            return -1
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'

if __name__ == "__main__":

    print("\n\n\n")
    player1 = input("\tEnter the name of Player 1: ")
    player2 = input("\tEnter the name of Player 2: ")
    current_player = player1
    if current_player == player1:
        player_value = "player1[X]"
    else:
        player_value = "player2[O]"

    player_choice = {'X': "", 'O': ""}
    turn_list = ['X', 'O']
    score_board = {player1: 0, player2: 0}
    Score_Board(score_board)
    while True:
        print("\t", player_value, "chance")
        player_choice['X'] = current_player
        if current_player == player1:
            player_choice['O'] = player2
        else:
            player_choice['O'] = player1

        winner = Play_Game(turn_list[0])

        if winner != -1:
            player_won = player_choice[winner]
        score_board[player_won] += 1
        Score_Board(score_board)
        if current_player == player1:
            current_player = player2
        else:
            current_player = player1
