import pygame

from constantes import Cores
from constantes import Configurations as conf


class Tabuleiro:

    def __init__(self, n):
        self.peca = None
        self.nome = n

    def iniciarTabuleiro(self, interface):

        interface.fill(Cores.preto)

        for col in range(conf.colunas):
            for lin in range(col % 2, conf.linhas, 2):
                pygame.draw.rect(interface, Cores.branco, (col * conf.quadrado, lin * conf.quadrado, conf.quadrado, conf.quadrado))
