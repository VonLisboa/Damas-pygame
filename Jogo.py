import pygame
from constantes import Cores
from Tabuleiro import Tabuleiro


class Jogo:

    def __init__(self):
        self._init()
        #self.win = win

    def _init(self):
        self.selecionado = None
        self.turn = Cores.vermelho
        self.valid_moves = {}

    def selecionaPeca(self, lin, col):
        print(lin)
        print(col)
        if self.selecionado:
            result = self._move(lin, col)
            if not result:
                self.selecionado = None
                self.selecionaPeca(lin, col)
        tabuleiro = Tabuleiro()
        Peca = tabuleiro.getPeca(lin, col)
        if Peca != 0 and Peca.cor == self.turn:
            self.selecionado = Peca
            #validar movimento
            return True

        return False

    def movimentaPeca(self, lin, col):
        tabuleiro = Tabuleiro()
        Peca = tabuleiro.getPeca(lin, col)

        ##
        return True