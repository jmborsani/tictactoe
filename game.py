#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

board = [["   ", "   ", "   "],["   ", "   ", "   "],["   ", "   ", "   "]]

p1 = raw_input("Jogador 1: ")
p2 = raw_input("Jogador 2: ")

players = [p1, p2]

print
print "Jogador {0} é X".format(p1)
print "Jogador {0} é O".format(p2)
print

def move(row, column, symb):
    board[row][column] = symb

def print_board(board):
    print "         |         |         "
    print "   {0}   |   {1}   |   {2}   ".format(board[0][0], board[0][1], board[0][2])
    print "---------|---------|---------"
    print "   {0}   |   {1}   |   {2}   ".format(board[1][0], board[1][1], board[1][2])
    print "---------|---------|---------"
    print "   {0}   |   {1}   |   {2}   ".format(board[2][0], board[2][1], board[2][2])
    print "         |         |         "

def how_to_play():
    board = [["0,0", "0,1", "0,2"],["1,0", "1,1", "1,2"],["2,0", "2,1", "2,2"]]
    print_board(board)

def get_coordenate(coordenate, board):
    coordenate = coordenate.split(",")
    try:
        row        = int(coordenate[0])
        column     = int(coordenate[1])

        if board[row][column] != "   ":
            print "Ops! O amiguinho já jogou aí!"
            return

        if (row < 0 or row > 2) or (column < 0 or column > 2):
            print "Ops! Esse campo não existe!"
            return

    except ValueError:
        print "Informe apenas números!"
        return

    except IndexError:
        print "Informe as coordenadas corretamente!"
        return

    return [row, column]

def who_wins(board):
    return False

print "Let's play!"
print
print_board(board)

start_with = random.randint(0,1)

if start_with == 1:
    players[0], players[1] = players[1], players[0]

i = 0
while True:
    i += 1
    print
    print "Turno #{0}. (h para help / s para mostrar o tabuleiro)".format(i)

    for i, player in enumerate(players):
        while True:
            coordenate = raw_input("{0}: ".format(player))

            if coordenate == "h":
                how_to_play()
                continue

            if coordenate == "s":
                print_board(board)
                continue

            # ToDo: sempre faz essa avaliacao!
            # Tirar do Loop
            if i == 0:
                symb   = " X "
            else:
                symb   = " O "

            coordenate = get_coordenate(coordenate, board)

            if coordenate == None:
                how_to_play()
                continue

            print
            move(coordenate[0], coordenate[1], symb)
            print_board(board)
            break

    if who_wins(board):
        continue
