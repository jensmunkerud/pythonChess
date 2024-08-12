pcs = ['♖','♜','♗','♝','♘','♞','♕','♛','♔','♚','♙','♟']


# Returns y, x
def translateCoords(coord):	# Translates since coords are on A2, H8 format
	x = coord[0]
	y = coord[1]
	wordies = "abcdefgh"
	for i in range(0, len(wordies)):
		if x.lower() == wordies[i]:
			return 8-int(y), i


def reverseTranslate(y, x):
	alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
	coord = ""
	coord += alphabet[x] + str(8-y)
	return coord


def isCorrectMove(pieceCoord): # Checks if move is even within the game limits
	try:
		if (int(pieceCoord[1]) in [1, 2, 3, 4, 5, 6, 7, 8]) and (pieceCoord[0] in "abcdefgh"):
			return True
		return False
	except:
		return False

def movePiece(pieceCoord, target, board):	#Actually performs the moving of pieces
	pcsY, pcsX = translateCoords(pieceCoord)
	trgY, trgX = translateCoords(target)
	board[trgY][trgX] = board[pcsY][pcsX]
	board[pcsY][pcsX] = " "


def isYourPiece(pieceCoord, whiteTurn, board):	# Checks if the piece you try to move is yours based on team
	pcsY, pcsX = translateCoords(pieceCoord)
	if board[pcsY][pcsX] == " ":
		return False
	elif board[pcsY][pcsX] in "♜♝♞♛♚♟":
		return True if whiteTurn else False
	else:
		return False if whiteTurn else True


# Cant just take not isYourPiece, because that would be true for empty positions
def isOpponent(pieceCoord, whiteTurn, board):	# Checks if the piece you try to move is not yours based on team
	pcsY, pcsX = translateCoords(pieceCoord)
	if board[pcsY][pcsX] == " ":
		return False
	elif board[pcsY][pcsX] in "♜♝♞♛♚♟":
		return False if whiteTurn else True
	else:
		return True if whiteTurn else False
	

# Same as above, in absolute coordinates
def absoluteIsOpponent(pcsY, pcsX, whiteTurn, board):	# Checks if the piece you try to move is yours based on team
	if board[pcsY][pcsX] == " ":
		return False
	elif board[pcsY][pcsX] in "♜♝♞♛♚♟":
		return False if whiteTurn else True
	else:
		return True if whiteTurn else False
	

# Same as above, only true for air additionally
def absoluteKillable(pcsX, pcsY, whiteTurn, board):	# True for clear and opponent pieces
	if board[pcsY][pcsX] == " ":
		return True
	elif board[pcsY][pcsX] in "♜♝♞♛♚♟":
		return False if whiteTurn else True
	else:
		return True if whiteTurn else False
	

# Tests if any pawn should be promoted after each move
def checkPawnPromotion(board):
	for row in range(0, 8):
		for column in range(0, 8):
			if board[row][column] == '♙' and row == 7:
				print("tried promote black")
				board[row][column] = '♕'
			elif board[row][column] == '♟' and row == 0:
				print("tried promote white")
				board[row][column] = '♛'