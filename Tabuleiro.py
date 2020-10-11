import pygame

from constantes import *

class Tabuleiro:


    def __init__(self, n):
        self.peca = None
        self.nome = n


    def iniciarTabuleiro(self, interface):

        interface.fill(preto)

        for col in range(colunas):
            for lin in range(col % 2, linhas, 2):
                pygame.draw.rect(interface, rosaClaro, (col * quadrado, lin * quadrado, quadrado, quadrado))

