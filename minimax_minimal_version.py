#0 1 2
#3 4 5
#6 7 8
import os
import time
field = 3
human = 'H'
computer = 'C'
clean_board = [0,1,2,3,4,5,6,7,8]
minimax_board = []

def win(tmp_board, player):
	if((tmp_board[0] == player and tmp_board[1] == player and tmp_board[2] == player) or
	(tmp_board[3] == player and tmp_board[4] == player and tmp_board[5] == player) or
	(tmp_board[6] == player and tmp_board[7] == player and tmp_board[8] == player) or
	(tmp_board[0] == player and tmp_board[3] == player and tmp_board[6] == player) or
	(tmp_board[1] == player and tmp_board[4] == player and tmp_board[7] == player) or
	(tmp_board[2] == player and tmp_board[5] == player and tmp_board[8] == player) or
	(tmp_board[0] == player and tmp_board[4] == player and tmp_board[8] == player) or
	(tmp_board[2] == player and tmp_board[4] == player and tmp_board[6] == player)):
		return 1
	else:
		return 0

def free_moves(tmp_board):
	free_moves_arr = []
	for i in range(0, field*field):
		if(tmp_board[i] != human and tmp_board[i] != computer):
			free_moves_arr.append(i)
	return free_moves_arr

def minimax(tmp_board, player):
	empty_cells = []
	empty_cells = free_moves(tmp_board)
	
	if(win(tmp_board, human)):
		return 0,-10
	elif(win(tmp_board, computer)):
		return 0,10
	elif not empty_cells:
		return 0,0
		
	moves = [[0]*2 for n in range(0,len(empty_cells))]
	
	for i in range(0,len(empty_cells)):
		moves[i][0] = empty_cells[i]
		tmp_board[empty_cells[i]] = player
		if(player == human):
			move, score = minimax(tmp_board, computer)
			moves[i][1] = score
		elif(player == computer):
			move, score = minimax(tmp_board, human)
			moves[i][1] = score
		tmp_board[empty_cells[i]] = 0

	move = 0
	if(player == human):
		score = 100
		for i in range(0,len(empty_cells)):
			if(moves[i][1] < score):
				score = moves[i][1]
				move = i
	else:
		score = -100
		for i in range(0,len(empty_cells)):
			if(moves[i][1] > score):
				score = moves[i][1]
				move = i
	return moves[move][0], moves[move][1]
	
def main():
	os.system('clear')
	board = clean_board
	menu = 1
	who_moves = 1
	while(not(win(board,human)) and not(win(board,computer)) and free_moves(board)):
		print(board)
		if(who_moves == 1):
			print('your move:')
			movement = int(input())
			if(str(board[movement]).isdigit()):
				board[movement] = human
				who_moves = 0
			else:
				print('incorrect move')
		else:
			print('computer moves:')
			minimax_board = board
			move, score = minimax(minimax_board, computer)
			board[move] = computer
			who_moves = 1
	print(board)
	if(win(board,human)):
		print('human wins')
	elif(win(board,computer)):
		print('computer wins')
	else:
		print('draw')
		
if __name__ == "__main__":
	main()