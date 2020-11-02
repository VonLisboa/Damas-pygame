import pygame

class Tabuleiro:

    def __init__(self, n):
        self.peca = None
        self.nome = n

    def iniciarTabuleiro(self, interface, conf):

        interface.fill(conf.corA)

        for col in range(conf.colunas):
            for lin in range(col % 2, conf.linhas, 2):
                pygame.draw.rect(interface, conf.corB, (col * conf.quadrado, lin * conf.quadrado, conf.quadrado, conf.quadrado))
