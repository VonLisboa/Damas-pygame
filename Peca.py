import pygame

from constantes import Cores


class Peca:
    PADDING = 15
    OUTLINE = 5

    def __init__(self, lin, col, cor, tamQuadrado):
        self.lin = lin
        self.col = col
        self.cor = cor
        self.rei = False
        self.x = 0
        self.y = 0
        self.tamQuadrado = tamQuadrado
        self.calcular()

    def converterPosicao(self):
        self.x = int(self.tamQuadrado * self.col + self.tamQuadrado / 2)
        self.y = int(self.tamQuadrado * self.lin + self.tamQuadrado / 2)

    def iniciarPeca(self, interface):
        margem = 10
        pecaTam = int(self.tamQuadrado/2 - margem)
        pygame.draw.circle(interface, self.cor, (self.x, self.y), pecaTam)

    def setRei(self):
        self.rei = True

    def mover(self, lin, col):
        self.lin = lin
        self.col = col
        self.calcular()

    def calcular(self):
        self.x = self.tamQuadrado * self.col + self.tamQuadrado // 2
        self.y = self.tamQuadrado * self.lin + self.tamQuadrado // 2

    def desenhar(self, display):
        # rainha = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))
        radius = self.tamQuadrado // 2 - self.PADDING
        pygame.draw.circle(display, Cores.cinza, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(display, self.cor, (self.x, self.y), radius)
        if self.rei:
            pygame.draw.circle(display, Cores.amarelo, (self.x, self.y), radius/2)
            #display.blit(rainha, (self.x - rainha.get_width() // 2, self.y - rainha.get_height() // 2))
