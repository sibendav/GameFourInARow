# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:58:25 2020


@author: Simha Ben-David (209166776) & Efrat Anconina (322796749)
    
"""


import game

board=game.game()
game.create(board)
print("Initial Game")
game.printState(board)
game.decideWhoIsFirst(board)
while not game.isFinished(board):
    print("continue game")
    if game.isHumTurn(board):
        game.inputMove(board)
    else:
        board=game.inputComputer(board)
    game.printState(board)

print("Game Over:")