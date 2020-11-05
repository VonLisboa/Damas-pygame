import pygame

from Tabuleiro import Tabuleiro
from constantes import Cores


class Jogo:
    def __init__(self, display, conf):
        self.conf = conf
        self.display = display
        self.setup()

    def setup(self):
        self.selecionado = None
        self.tabuleiro = Tabuleiro("meuTab", self.conf)
        self.tabuleiro.desenharTabuleiro(self.display)
        self.vez = Cores.azul
        self.movimentosValidos = {}

    def update(self):
        self.tabuleiro.desenharPecas(self.display)
        self.desenhaMovimentosValidos(self.movimentosValidos)

    def ganhador(self):
        return self.tabuleiro.ganhador()

    def reset(self):
        self.setup()

    def seleciona(self, lin, col):
        if self.selecionado:
            if not self._mover(lin, col):
                self.selecionado = None
                self.seleciona(lin, col)

        peca = self.tabuleiro.getPeca(lin, col)
        if peca != 0 and peca.cor == self.vez:
            self.selecionado = peca
            self.movimentosValidos = self.tabuleiro.getMovimentosValidos(peca)
            return True

        return False

    def _mover(self, lin, col):
        peca = self.tabuleiro.getPeca(lin, col)
        if self.selecionado and peca == 0 and (lin, col) in self.movimentosValidos:
            self.tabuleiro.movimentar(self.selecionado, lin, col)
            capturado = self.movimentosValidos[(lin, col)]
            if capturado:
                self.tabuleiro.remover(capturado)
            self.mudarVez()
        else:
            return False
        return True

    def desenhaMovimentosValidos(self, movimentos):
        tam = self.conf.getTamanhoQuadrado()
        for m in movimentos:
            lin, col = m
            pygame.draw.rect(self.display, Cores.amareloClaro,
                             (col * tam-7 + tam // 8,lin * tam-7 + tam // 8, tam, tam))

    def mudarVez(self):
        self.movimentosValidos = {}
        if self.vez == Cores.azul:
            self.vez = Cores.vermelho
        else:
            self.vez = Cores.azul