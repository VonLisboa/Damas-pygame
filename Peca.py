import pygame


class Peca:
    def __init__(self, lin, col, cor):
        self.lin = lin
        self.col = col
        self.cor = cor
        self.king = False
        self.x = 0
        self.y = 0

    def definirPosicao(self, quadradoTam):
        self.x = int(quadradoTam * self.col + quadradoTam / 2)
        self.y = int(quadradoTam * self.lin + quadradoTam / 2)


    def iniciarPeca(self, interface, quadradoTam):
        margem = 10
        pecaTam = int(quadradoTam/2 - margem)
        pygame.draw.circle(interface, self.cor, (self.x, self.y), pecaTam)


