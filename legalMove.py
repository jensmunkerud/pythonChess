from functionLibrary import *

#♖♜♗♝♘♞♕♛♔♚♙♟

# pcsX is the x coordinate of the piece in listSpace
# pcsY is the y coordinate of the piece in listSpace
# Same for trgX / trgY, only that it is target

# Board coordinate system, done differently in the other files, correct here
#	 y
#	0|
#	1|
# 	3|
#	6|
#	8|
#	 ----------- x
#	  0 1 3 6 8

def isLegalMove(pieceCoord, target, board, whiteTurn):	#Checks if move is at all possible
	pcsY, pcsX = translateCoords(pieceCoord)	#The first variable really is the height of pcs
	trgY, trgX = translateCoords(target)		#Same here
	
	match board[pcsY][pcsX]:

		# Can still move two after first move
		case '♟':	#White pawn, subtracting cauze 0 is on top of list, -1 is upwards..
			if abs(trgX - pcsX) == 1 and pcsY - trgY == 1:	#Kill diagonally
				return isOpponent(target, whiteTurn, board)		#Critical check, so we dont always allow diagonal
			
			elif board[pcsY - 1][pcsX] == " " and pcsX == trgX:	#Checks if clear one up
				if pcsY - trgY == 1:
					return not isYourPiece(target, whiteTurn, board)
				
				elif pcsY - trgY == 2:			#Checks if clear two up
					if board[pcsY - 2][pcsX] == " " and pcsY == 6:	
						return not isYourPiece(target, whiteTurn, board)
					else:
						return False
				else:
					return False
			else:
				return False
			

		case '♙':	#Black pawn, adding cauze 0 is on top of list, +1 is downwards..
			if abs(trgX - pcsX) == 1 and pcsY - trgY == -1:	#Kill diagonally
				return isOpponent(target, whiteTurn, board)
			
			elif board[pcsY + 1][pcsX] == " " and pcsX == trgX:	#Checks if clear one down
				if pcsY - trgY == -1:
					return not isYourPiece(target, whiteTurn, board)
				
				elif pcsY - trgY == -2:			#Checks if clear two down
					if board[pcsY + 2][pcsX] == " " and pcsY == 1:
						return not isYourPiece(target, whiteTurn, board)
					else:
						return False
				else:
					return False
			else:
				return False
		

		case '♖' | '♜':
			if pcsX == trgX:		# Moving up and down

				x = -1 if pcsY > trgY else 1	#important multiplier nbd, If true, we want to go up (-1)
				for i in range(pcsY + x, trgY, x):				
					if board[i][pcsX] != " ":
						return False
				if isYourPiece(target, whiteTurn, board):
					return False
				return True
				
			elif pcsY == trgY:		#Moving left and right

				x = 1 if trgX > pcsX else -1	#important multiplier nbd, If true, we want to go down (+1)
				for i in range(pcsX + x, trgX, x):				
					if board[pcsY][i] != " ":
						return False
				if isYourPiece(target, whiteTurn, board):
					return False
				return True

			else:
				return False	#Neither x or y axis was similar between pcs and trg, rook can only move one axis at a time


		case '♘' | '♞':
			relativeValidPositions = [[1, 2], [2, 1], [2, -1], [1, -2], [-1, -2], [-2, -1], [-2, 1], [-1, 2]]
			for pos in relativeValidPositions:
				try:
					if pcsX + pos[0] == trgX and pcsY + pos[1] == trgY:
						return absoluteKillable(pcsX + pos[0], pcsY + pos[1], whiteTurn, board)
				except:
					continue
			return False
	

		case '♔' | '♚':
			relativeValidPositions = [[0,1], [1,1], [1,0], [1,-1], [0,-1], [-1,-1], [-1,0], [-1,1]]
			for pos in relativeValidPositions:
				try:
					if pcsX + pos[0] == trgX and pcsY + pos[1] == trgY:
						return absoluteKillable(pcsX + pos[0], pcsY + pos[1], whiteTurn, board)
				except:
					continue
			return False
		

		case '♗' | '♝':
			if abs(pcsX - trgX) == abs(pcsY - trgY):	#Confirmed, we are trying to go diagonally
				xDir = 1 if trgX > pcsX else -1
				yDir = 1 if trgY > pcsY else -1
				for i in range(1, abs(trgX - pcsX)):
					if board[pcsY + i * yDir][pcsX + i * xDir] != " ":
						return False
				return not isYourPiece(target, whiteTurn, board)
			else:
				return False


		case '♕' | '♛':
			if pcsX == trgX:		# Moving up and down

				x = -1 if pcsY > trgY else 1	#important multiplier nbd, If true, we want to go up (-1)
				for i in range(pcsY + x, trgY, x):				
					if board[i][pcsX] != " ":
						return False
				if isYourPiece(target, whiteTurn, board):
					return False
				return True
				
			elif pcsY == trgY:		# Moving left and right

				x = 1 if trgX > pcsX else -1	# important multiplier nbd, If true, we want to go down (+1)
				for i in range(pcsX + x, trgX, x):				
					if board[pcsY][i] != " ":
						return False
				if isYourPiece(target, whiteTurn, board):
					return False
				return True

			elif abs(pcsX - trgX) == abs(pcsY - trgY):	# Diagonally
				xDir = 1 if trgX > pcsX else -1
				yDir = 1 if trgY > pcsY else -1
				for i in range(1, abs(trgX - pcsX)):
					if board[pcsY + i * yDir][pcsX + i * xDir] != " ":
						return False
				return not isYourPiece(target, whiteTurn, board)
			else:
				return False


		case _:
			print("Invalid piece?!?!?!")
			return False
