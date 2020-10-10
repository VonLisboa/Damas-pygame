import pygame

from constantes import *

class Tabuleiro:


    def __init__(self, n):
        self.tab = []
        self.peca = None
        self.nome = n


    def iniciarTabuleiro(self, interface):

        interface.fill(preto)

        for col in range(colunas): # 0 ate 7 -> 0-1-2-3-4-5-6-7
            for lin in range(col % 2, linhas, 2): # 0 ate 7 -> 0-2-4-6-8
                pygame.draw.rect(interface, rosaClaro, (col * quadrado, lin * quadrado, quadrado, quadrado))

