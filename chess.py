import copy
from boardGenerator import *
from functionLibrary import *
import legalMove
import checkFunc


def main():
	board = generateBoard()
	whiteTurn = True
	message = ""
	while not checkFunc.isCheckMate(board, whiteTurn):
		refreshBoard(board)	#Draws board in its current state
		print(message)
		message = "" 


		# Loops until user inputs a valid coordinate for PIECE
		move = input(f"{'White' if whiteTurn else 'Black'} turn! Choose a piece: ")
		while not isCorrectMove(move):
			refreshBoard(board)
			print("That move is off limits!")
			move = input(f"{'White' if whiteTurn else 'Black'} turn! Choose a piece: ")


		# Loops until valid piece is selected
		while not isYourPiece(move, whiteTurn, board):
			refreshBoard(board)
			print("That is not your piece!")
			move = input(f"{'White' if whiteTurn else 'Black'} turn! Choose a piece: ")
		

		# Shows pieces valid moves
		displayPiecePath(board, move, whiteTurn)


		# Loops until user input valid coordinate for TARGET
		target = input("Move to: ")
		while not isCorrectMove(target):
			print("That move is off limits!")
			target = input("Move to: ")


		# Starts gameloop again if move given is illegal, having to select piece again etc.
		if not legalMove.isLegalMove(move, target, board, whiteTurn):	
			message = "You prolly cant move that piece..."
			continue #sweet


		# Before doing move, even if its valid in itself
		# checks if own king gets checked in that future game state..
		testBoard = copy.deepcopy(board) 
		movePiece(move, target, testBoard)
		if checkFunc.isCheck(whiteTurn, testBoard):
			message = "That move would be suicide! You have to protect the king"
			continue


		# Finally moves piece and switches player
		movePiece(move, target, board)	
		message = ""
		print("Move performed, switching teams")
		whiteTurn = not whiteTurn
		
		# Checks if a pawn should be promoted
		checkPawnPromotion(board)

		# Check if this move set opponent king in check!
		if checkFunc.isCheck(whiteTurn, board):
			message = f"{'White' if whiteTurn else 'Black'} is in check!"

		# Next game loop

	# Game has ended
	refreshBoard(board)
	print(f"{'Black' if whiteTurn else 'White'} WON!!")
	input()
main()