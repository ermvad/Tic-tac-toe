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
	"""
	Фунция win проверят на достижение одного терминального состояния (победа)
	В качестве параметров передется игрок (для которого проверяется состояние) и поле
	Функция должна вернуть число, ранвое 1, если данный игрок победил, в остальных случаях 0
	Блок схема приведена в директории scheme
	Входные параметры:
		tmp_board - игровое поле
		player - игрок, для которого проверяется одно терминальное состояние (победа)
	Выходные параметры:
		int: 1 - данный игрок победил, 0 остальные случаи
	Пример:
			board:
			X 0 X
			X X
			0 0 0
		c = win(board, computer)
		h = win(board, human)
		print(k)
		>1
		print(h)
		>0
	Задача:
		1. Реализуйте данную функцию
		2. Проверьте функцию с помощью тестов
	"""

def free_moves(tmp_board):
	"""
	Функция free_moves возвращает список с индексами незанятых клеток.
	Блок схема приведена в директории scheme
	Входные параметры:
		tmp_board - игровое поле
	Выходные параметры:
		free_moves_arr - список индексов пустых клеток
	Пример:
			board:
			  0 X
			X X
			0   0
		e = []
		e = free_moves(board)
		print(e)
		>[0, 5, 7]
	Здача:
		1. Реализуйте следующее:
		1.1 Условие оператора if
		1.2 Добавление в список free_moves_arr индекса пустой клетки
		2. Проверьте функцию с помощью тестов
	"""
	free_moves_arr = []
	for i in range(0, field*field):
		if("""клетка пуста"""):
			"""добавить индекс пустой клетки в список free_moves_arr"""
	return free_moves_arr

def minimax(tmp_board, player):
	"""
	Функция minimax вызвращает оптимальный индекс клетки для хода, и стоимость хода. Функция рекурсивна. Выполняется до тех пор пока не будут перебраны все свободные клетки или достигнуто терминальное состояние для рекурсивных вызовов
	После вызова функции первым делом проверяются 3 терминальных состояния: победа для заданного player, поражение или ничья. При достижении этих состояний возвращается счет, а в качестве индекса клетки возвращается -1, так как индекс на данный момент особо нас не инетесует.
	Затем получаем индексы пустых клеток. После происходит сбор очков с пустых клеток следующим образом. В цикле выполняем ход за текущего игрока на текущее поле в пустую клетку, предварительно запомнив индекс данной клетки (в список moves). Далее рекурсивно вызываем minimax для оппонента (другого игрока), поместив возвращенное значение счета в список moves.
	После выхова minimax для другого игрока сделаем отмену хода за текущего игрока и выполним новую итерацию цикла. Новая итерация цикла будет для следующей свободной клетки. Таким образом с точки зрения теории графа выполняется обход всех ветвей данного графа.
	После того, как очки для каждой клетки со всех клеток собраны необходимо выбрать наилучший ход:
		Для человека - ход с наименишим количеством очков - MINI
		Для компьюетера - ход с наибольшим колическтвом очков - MAX
	Наилучший ход ищется в списке moves по индексу 1. Если наилучних ходов несколько, выбирается из списка
	После того как такой ход найден, функция возвращает данный ход (индекс клетки) и счет для него.
	Псевдокод:
		получить_свободные_клетки;
		проверить_на_терминальное_сотояние;
		цикл по свободным_клеткам
			сделать_ход_за_текущего_игрока
			вызвать минимакс(оппонент)

	Блок схема приведена в директории scheme
	Входные параметры:
		tmp_board - игровое поле
		player - игрок, для которого проверяется одно терминальное состояние (победа)
	Выходные параметры:
		int,int: индекс клетки для наилучшего хода, стоимость хода
	"""
	empty_cells = []
	empty_cells = free_moves(tmp_board)

	if(win(tmp_board, human)):
		return -1,-10

	#
	#
	#
	#
	#

	elif not empty_cells:
		return -1,0

	moves = [[0]*2 for n in range(0,len(empty_cells))]

	for i in range(0,len(empty_cells)):
		moves[i][0] = empty_cells[i]
		tmp_board[empty_cells[i]] = player
		#
		#
		#
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
		#
		#
		#
		#
		#
	return moves[move][0], moves[move][1]

def main():
	board = clean_board
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