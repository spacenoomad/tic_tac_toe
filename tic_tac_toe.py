running = True
_board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]

slot_empty = "-"
slot_p1 = "X"
slot_p2 = "0"


def p1_win():
	global running
	running = False
	print("player 1 won!")
	
def p2_win():
	global running
	running = False
	print("player 2 won!")

def _tie():
	global running
	running = False
	print("game over, it's a tie!")
	
def _winning():
	for i in range(0, 7, 3):
		if _board[i] == _board[i+1] and _board[i] == _board[i+2] and not _board[i] == "-":
			if _board[i] == "X":
				p1_win()
			else: 
				p2_win()
	for i in range(0, 3):
		if _board[i] == _board[i+3] and _board[i] == _board[i+6] and not _board[i] == "-":
			if _board[i] == "X":
				p1_win()
			else: 
				p2_win()
				
	
	if _board[0] == _board[4] and _board[0] == _board[8] and not _board[0] == "-":
		if _board[0] == "X":
			p1_win()
		else: 
			p2_win()
			
	elif _board[2] == _board[4] and _board[2] == _board[6] and not _board[2] == "-":
		if _board[2] == "X":
			p1_win()
		else: 
			p2_win()

print("welcome to a game of tic tac toe. player 1 starts first")

print(" " + _board[0] + " | " + _board[1] + " | " + _board[2] + " ")
print("----------")
print(" " + _board[3] + " | " + _board[4] + " | " + _board[5] + " ")
print("----------")
print(" " + _board[6] + " | " + _board[7] + " | " + _board[8] + " ")

while running:
	 
	while True:
		try: 
			p_1 = int(input("choose where to place a cross player 1 (0-8): "))
			if not _board[p_1] == "-":
				print("this spot is already taken")
			else: 
				_board[p_1] = "X"
				break
		except:
			print("that's not a valid input, try again")

	print(" " + _board[0] + " | " + _board[1] + " | " + _board[2] + " ")
	print("----------")
	print(" " + _board[3] + " | " + _board[4] + " | " + _board[5] + " ")
	print("----------")
	print(" " + _board[6] + " | " + _board[7] + " | " + _board[8] + " ")
	
	_winning()
	
	
	if running == False:
		break
	
	i = 0
	count_empties = 0
	for i in range(0, 9):
		if _board[i] == slot_empty:
			count_empties += 1
		i += 1
	if count_empties == 0:
		_tie()
		
	if running == False:
		break
	
	while True:
		try: 
			p_2 = int(input("it's player 2's turn. choose where to put a zero (0-8): "))
			if not _board[p_2] == "-":
				print("this spot is already taken")
			else: 
				_board[p_2] = "0"
				break
		except:
			print("that's not a valid input, try again")
			
	print(" " + _board[0] + " | " + _board[1] + " | " + _board[2] + " ")
	print("----------")
	print(" " + _board[3] + " | " + _board[4] + " | " + _board[5] + " ")
	print("----------")
	print(" " + _board[6] + " | " + _board[7] + " | " + _board[8] + " ")
	
	_winning()

