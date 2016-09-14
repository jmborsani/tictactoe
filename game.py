#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def create_board():
    return list([" " for i in range(1,10)])

def get_players():
    p1 = raw_input("Jogador 1: ")
    p2 = raw_input("Jogador 2: ")

    return [p1, p2]

def print_board(board):
    print "   {0}   |   {1}   |   {2}   ".format(board[0], board[1], board[2])
    print "{0}|{0}|{0}".format("-" * 7)
    print "   {0}   |   {1}   |   {2}   ".format(board[3], board[4], board[5])
    print "{0}|{0}|{0}".format("-" * 7)
    print "   {0}   |   {1}   |   {2}   ".format(board[6], board[7], board[8])

def how_to_play():
    board = list(range(1,10))
    print_board(board)

def verify_input(user_input, board):
    position = 0

    try:
        position = int(user_input)

        if (position < 1 or position > 9):
            position = 0
            raise IndexError("Ops! Essa posição não existe!")

    except ValueError:
        print "Ops! Informe apenas números!"

    except IndexError as msg:
        print msg

    return position

def who_wins(board):
    return False

def move(position, symb):
    pos = position - 1

    if board[pos] != " ":
        print "Ops! O amiguinho já jogou aí!"
        return False

    board[pos] = symb
    return True

if __name__ == "__main__":
    # criando tabuleiro
    board = create_board()

    # pegando os jogadores
    players = get_players()

    # imprimindo o tabuleiro e como jogar
    print "Let's play!"
    how_to_play()

    # randomizando a ordem de jogada
    start_with = random.randint(0,1)

    if start_with == 1:
        players[0], players[1] = players[1], players[0]

    # definicao dos simbolos
    symbols = ["X", "O"]

    # imprimido ordem para o jogadores
    print "Jogador {0} é {1}".format(players[0], symbols[0])
    print "Jogador {0} é {1}".format(players[1], symbols[1])

    i = 0
    while True:
        i += 1
        print "Turno #{0}. ('h' para Help / 's' para imprimir tabuleiro)".format(i)

        for j, player in enumerate(players):
            while True:
                user_input = raw_input("{0}: ".format(player)).rstrip('\n')

                if user_input == "h":
                    how_to_play()
                    continue

                if user_input == "s":
                    print_board(board)
                    continue

                position = verify_input(user_input, board)

                if position == 0:
                    how_to_play()
                    continue

                if move(position, symbols[j]):
                    print_board(board)
                    break

        if who_wins(board):
            continue
