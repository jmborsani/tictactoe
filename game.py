#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, sys

def boards():
    return list(range(1,10)), list([" " for i in range(1,10)])

def get_players():
    p1 = raw_input("Jogador 1: ").upper()
    p2 = raw_input("Jogador 2: ").upper()

    return [p1, p2]

def print_board(board):
    print '''
    {}   |   {}   |   {}
  ----- + ----- + -----
    {}   |   {}   |   {}
  ----- + ----- + -----
    {}   |   {}   |   {}
    '''.format(board[0], board[1], board[2], board[3], board[4], board[5], board[6], board[7], board[8])

def how_to_play():
    print '''
    1   |   2   |   3
  ----- + ----- + -----
    4   |   5   |   6
  ----- + ----- + -----
    7   |   8   |   9
    '''

def verify_input(user_input):
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
    if board[0] == board[1] and board[1] == board[2]:
        return True
    if board[3] == board[4] and board[4] == board[5]:
        return True
    if board[6] == board[7] and board[7] == board[8]:
        return True
    if board[0] == board[3] and board[3] == board[6]:
        return True
    if board[1] == board[4] and board[4] == board[7]:
        return True
    if board[2] == board[5] and board[5] == board[8]:
        return True
    if board[0] == board[4] and board[4] == board[8]:
        return True
    if board[2] == board[4] and board[4] == board[6]:
        return True

    return False

def verify_position(user_input):
    position = (user_input - 1)

    if board[position] == "X" or board[position] == "O":
        print "Ops! O amiguinho já jogou aí!"
        return False

    return True

def move(board, user_board, position, symb):
    pos = position - 1
    board[pos] = symb
    user_board[pos] = symb


def end_game():
    sys.exit(1)

if __name__ == "__main__":
    # variaveis de loop game and playing
    playing = True

    # criando tabuleiros
    board, user_board = boards()

    # pegando os jogadores
    players = get_players()

    # imprimindo o tabuleiro e como jogar
    print "\n\nLet's play!\n\n".upper()
    how_to_play()

    # randomizando a ordem de jogada
    start_with = random.randint(0,1)

    if start_with == 1:
        players[0], players[1] = players[1], players[0]

    # definicao dos simbolos
    symbols = ["X", "O"]

    # imprimido ordem para o jogadores
    print "\n\n* Jogador {0} é {1}".format(players[0], symbols[0])
    print "* Jogador {0} é {1}\n\n".format(players[1], symbols[1])

    turn = 0
    while True:
        for i, player in enumerate(players):
            playing = True
            turn += 1

            if turn >= 10:
                print "Não houve ganhador, deu velha!"
                end_game()

            while playing:
                print "Turno #{0}\t\t(h help | s board)".format(turn)

                user_input = raw_input("{0}: ".format(player).rstrip('\n'))

                if user_input == "h":
                    how_to_play()
                    continue

                if user_input == "s":
                    print_board(user_board)
                    continue

                position = verify_input(user_input)
                position_valid  = verify_position(position)

                if not position or not position_valid:
                    print ""
                    how_to_play()
                    continue

                move(board, user_board, position, symbols[i])
                print_board(user_board)

                if who_wins(board):
                    print "Jogador {0} ganhou, parabéns!".format(player)
                    end_game()
                else:
                    playing = False
