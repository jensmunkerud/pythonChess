from functionLibrary import *
from legalMove import *
import copy

# Supposed to see if king is in check
# if White -> see if white king is attacked by black
# A check has to be made for each piece`s way of attacking

def isCheck(whiteTurn, board, kingAbsX = -1, kingAbsY = -1):
	print(f"Checking if {'White' if whiteTurn else 'Black'} is in check")

	if kingAbsX >= 0 and kingAbsY >= 0:
		kingX, kingY = kingAbsX, kingAbsY
		print("We are doing absolute position check!")
	else:

		# Finds kings position on our own
		kingX = 0
		kingY = 0
		for i in range(0, 8):
			for j in range(0, 8):
				if whiteTurn and board[i][j] == "♚":
					kingX = j
					kingY = i
				elif not whiteTurn and board[i][j] == "♔":
					kingX = j
					kingY = i
				
		print(f"king position is y:{kingY} , x:{kingX}")


	# See if we are attacked by knight
	relativeValidPositions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
	for pos in relativeValidPositions:
		# CRUCIAL CHECK!! if not we might check for knights in negative positions
		# IE looping to other side of the list..... important shit
		if kingY + pos[1] >= 0 and kingX + pos[0] >= 0: 
			try:
				if whiteTurn and board[kingY + pos[1]][kingX + pos[0]] == '♘':
					print("We def not good")
					return True 
				elif not whiteTurn and board[kingY + pos[1]][kingX + pos[0]] == '♞':
					print("We def not good")
					return True
			except:
				# pos to be checked was outside board limits
				continue

	
	# See if we are attacked by a rook or queen
	vectorDirections = [[1, 0], [0, 1], [-1, 0], [0, -1]]
	for dir in vectorDirections:
		iterator = 1
		try:
			# Might be a bug here where negative positions can overflow to opposite side of board
			# only situational when using absolute positions..
			while board[kingY + dir[0] * iterator][kingX + dir[1] * iterator] == " ":
				iterator += 1
				if iterator >= 8:
					break
		except:
			continue
		
		# After while loop, we should either hit something or run out of iterators.
		# We then check if that last element was enemy queen or rook, based on team
		if kingY + dir[0] * iterator >= 0 and kingX + dir[1] * iterator >= 0:
			try:
				if board[kingY + dir[0] * iterator][kingX + dir[1] * iterator] in (("♖♕") if whiteTurn else ("♜♛")):
					print("Check by queen or rook")
					return True
			except:
				continue


	# See if we are attack by bishop or queen
	vectorDirections = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
	for dir in vectorDirections:
		iterator = 1
		try:
			while board[kingY + dir[0] * iterator][kingX + dir[1] * iterator] == " ":
				iterator += 1
				if iterator >= 8:
					break
		except:
			continue
		
		# After while loop, we should either hit something or run out of iterators.
		# We then check if that last element was enemy queen or rook, based on team
		if kingY + dir[0] * iterator >= 0 and kingX + dir[1] * iterator >= 0:
			try:
				if board[kingY + dir[0] * iterator][kingX + dir[1] * iterator] in (("♗♕") if whiteTurn else ("♝♛")):
					print(f"y: {kingY + dir[0] * iterator}, x: {kingX + dir[1] * iterator}")
					print("Check by queen or bishop")
					return True
			except:
				continue


	# See if we are attacked by pawn
	if whiteTurn:
		for pos in [[-1, 1], [-1, -1]]:
			try:
				if board[kingY + pos[0]][kingX + pos[1]] == '♙':
					return True
			except:
				continue

	elif not whiteTurn:
		for pos in [[1, 1], [1, -1]]:
			try:
				if board[kingY + pos[0]][kingX + pos[1]] == '♟':
					return True
			except:
				continue
	

	# See if we are attacked by King (There really is no check for kings killing eachother yet..)
	for pos in [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]:	# All relative kings positions
		if kingY + pos[0] >= 0 and kingX + pos[1] >= 0:
			try:
				if board[kingY + pos[0]][kingX + pos[1]] == ('♔' if whiteTurn else '♚'):
					return True
			except:
				continue



	print(f"{'White' if whiteTurn else 'Black'} king is not attacked :)")
	return False



# Checkmate must also check for other pieces possibly blocking the attacking piece,
# not only simulating the kings own possible moves and seeing if those are in check

def isCheckMate(board, whiteTurn):	# Supposed to check if king is in checkmate
	# Since this check is done right after opponent has done a move,
	# (Which BTW we already know dont put himself in check)
	# We can test this only once..

	# Finds kings position
	kingX = 0
	kingY = 0
	for i in range(0, 8):
		for j in range(0, 8):
			if whiteTurn and board[i][j] == "♚":
				kingX = j
				kingY = i
			elif not whiteTurn and board[i][j] == "♔":
				kingX = j
				kingY = i
			


	# Just do a isCheck test for every adjacent valid position of the king
	relativeKingPos = [[0, 0], [1, 0], [1, 1], [0, 1], [-1, 1], [-1, 0], [-1, -1], [0, -1], [1, -1]]
	for pos in relativeKingPos:
		print("searching")
		try:
			if board[kingY + pos[1]][kingX + pos[0]] in (' ♖♗♘♕♙' if whiteTurn else ' ♜♝♞♛♟'):	# Valid pieces king can kill and escape to simultaneously
				print(f"checkmating position y: {kingY + pos[1]}, x: {kingX + pos[0]}")
				if not isCheck(whiteTurn, board, kingX + pos[0], kingY + pos[1]):
					return False
				else:
					continue
		except:
			continue
	
	print("The king should'v be protected by another piece")

#	#♖♜♗♝♘♞♕♛♔♚♙♟
#	# If above fails, find every black/white piece and simulate every possible move
#	# to see if in any of those situations the king is not in checkmate
	ownPieces = []
	for y in range(0, 8):
		for x in range(0, 8):
			if board[y][x] in ['♖', '♗', '♘', '♕', '♙'] and not whiteTurn:
				ownPieces.append([y, x])
			elif board[y][x] in ['♜', '♝', '♞', '♛', '♟'] and whiteTurn:
				ownPieces.append([y, x])
			# Now we have saved every own pieces locations..

	for piece in ownPieces:
		# Positions to test has to be on A1, C4 format due to "isValidMove" is made that way
		# This could be improved, in fact this whole method is extremely unneccessary
		# Should translate position to 00, 01 immediately, only taking absolute positions in internal functions
		for y in range(1, 9):
			for x in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
				#print(f"piece {piece}  y:{y}, x:{x}")
				testMove = x + str(y)	# Move to be tested against
				if isCorrectMove(testMove):
					absPiecePos = reverseTranslate(piece[0], piece[1])
					if not isLegalMove(absPiecePos, testMove, board, whiteTurn):
						continue

					# Finally tests if this currently valid move doesnt put king in check
					pcsY, pcsX = piece[0], piece[1]
					trgY, trgX = translateCoords(testMove)
					testBoard = copy.deepcopy(board)
					testBoard[trgY][trgX] = testBoard[pcsY][pcsX]
					testBoard[pcsY][pcsX] = " "
					print("checked ///////////////////")
					if not isCheck(whiteTurn, testBoard):
						# Returns false if we find least ONE situation where king is not in checkmate
						return False
	# The king is in checkmate
	return True