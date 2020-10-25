import pygame
from MenuCustom import MenuCustom
from Tabuleiro import Tabuleiro
import pygame_menu
from constantes import Cores
from constantes import Configurations as conf
from constantes import tema

def main():
    running = True
    # clock = pygame.time.Clock()

    tab = Tabuleiro("meuTab")

    tab.iniciarTabuleiro(gamedisplay)

    pygame.display.update()
    while running:
        # clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # if event.type == pygame.MOUSEBUTTONDOWN:
            # pass

    pygame.quit()


def sobreOJogo():
    running = True
    gamedisplay.fill(Cores.rosaClaro)
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    textsurface = myfont.render('Trabalho sobre a materia ES2', False, (0, 0, 0))
    gamedisplay.blit(textsurface, (0, 0))
    pygame.display.update()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


pygame.init()

gamedisplay = pygame.display.set_mode((conf.largura, conf.altura))
pygame.display.set_caption("Jogo de Damas")

menu = MenuCustom(conf.largura, conf.altura, 'Bem-vindo', theme=tema)

menu.add_text_input('Name:', default='Lucas')
menu.add_button('Play', main)
menu.add_button('Configurações', sobreOJogo)
menu.add_button('Sobre', sobreOJogo)
menu.add_button('Quit', pygame_menu.events.EXIT)
menu.add_image("jogo-damas.jpg", angle=10, scale=(0.15, 0.15))

menu.mainloop(gamedisplay)
