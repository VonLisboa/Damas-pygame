import pygame

from constantes import *

from Tabuleiro import Tabuleiro

def main():
    pygame.init()

    gamedisplay = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo de Damas")

    running = True
    #clock = pygame.time.Clock()

    tab = Tabuleiro("meuTab")

    tab.iniciarTabuleiro(gamedisplay)

    pygame.display.update()
    while running:
        #clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            #if event.type == pygame.MOUSEBUTTONDOWN:
               # pass


    pygame.quit()

main()