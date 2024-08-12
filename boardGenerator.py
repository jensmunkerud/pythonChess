import os
import copy
from functionLibrary import *
import legalMove

pathChar = "•"

def generateBoard():
	board = [['♖', '♘', '♗', '♕', '♔', '♗', '♘', '♖'],
  			 ['♙', '♙', '♙', '♙', '♙', '♙', '♙', '♙'],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 ['♟', '♟', '♟', '♟', '♟', '♟', '♟', '♟'],
  			 ['♜', '♞', '♝', '♛', '♚', '♝', '♞', '♜']]
	
	board1 = [['♖', ' ', '♙', '♖', '♔', '♖', ' ', '♖'],
  			 ['♙', '♟', ' ', '♖', ' ', '♖', '♙', '♙'],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', '♚', ' ', ' ', ' ', ' ', ' '],
  			 [' ', ' ', '♙', ' ', ' ', ' ', ' ', ' '],
  			 ['♟', ' ', ' ', ' ', ' ', '♟', '♟', '♟'],
  			 [' ', '♞', ' ', '♛', ' ', '♝', '♞', '♜']]
	
	return board

def refreshBoard(board, markedPositions = []):

	# Puts x's where piece can move
	localBoard = copy.deepcopy(board)
	if len(markedPositions) > 0:
		for pos in markedPositions:
			if localBoard[pos[0]][pos[1]] == " ":
				localBoard[pos[0]][pos[1]] = pathChar

	os.system('cls' if os.name == 'nt' else 'clear')	# Clears screen
	print("     a    b    c    d    e    f    g    h")
	line = "  +————+————+————+————+————+————+————+————+"
	print(line)
	count = 8
	for row in localBoard:
		print(f"{count} | ", end="")	#Adds left row numbers
		for piece in row:
			print(piece, end="  | ")
		print(f"{count}\n{line}")		#Adds right row numbers
		count -= 1
	print("     a    b    c    d    e    f    g    h")


# Creates an 8x8 input matrix, testing every possible move for the given piece
# and sees if that move is legal, saving that position
# We then refresh the board with these positions as markers
def displayPiecePath(board, move, whiteTurn):
	temparr = []
	for i in range(1, 9):
		for j in ["a", "b", "c", "d", "e", "f", "g", "h"]:
			daniel = j + str(i)
			if isCorrectMove(daniel):
				if legalMove.isLegalMove(move, daniel, board, whiteTurn):
					y, x = translateCoords(daniel)
					temparr.append([y, x])
	refreshBoard(board, temparr)