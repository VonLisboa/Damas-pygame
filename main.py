import pygame
from pygame_menu import Menu
from Jogo import Jogo
from MenuCustom import MenuCustom
from Tabuleiro import Tabuleiro
import pygame_menu
from constantes import Cores
from Configurations import Configurations
from constantes import tema


def getPosicao(pos):
    x, y = pos
    lin = y // pos
    col = x // pos
    return int(lin), int(col)


def main():
    global conf
    running = True
    # clock = pygame.time.Clock()

    tab = Tabuleiro("meuTab")
    #tab.iniciarTabuleiro(gamedisplay, conf)
    tab.desenharPecas(gamedisplay, conf)

    pygame.display.update()

    jogo = Jogo()
    while running:
        # clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                lin, col = getPosicao(conf.getQuadrado())
                jogo.selecionaPeca(lin, col)

            # if event.type == pygame.MOUSEBUTTONDOWN:
            # pass

    pygame.quit()


def sobreOJogo():
    global gamedisplay
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

conf = Configurations()
gamedisplay = pygame.display.set_mode((conf.largura, conf.altura))
pygame.display.set_caption("Jogo de Damas")

main_menu = MenuCustom(conf.largura, conf.largura, 'Bem-vindo', theme=tema)
main_menu.add_text_input('Name:', default='Lucas')
main_menu.add_button('Play', main)

submenu = Menu(conf.largura, conf.largura, 'Configurações', theme=tema)


def submenu_cores(txt, i):
    conf.setCorTabuleiro(i)


def submenu_resolucao(txt, i):
    global main_menu, submenu
    largura, altura = conf.setResolucao(i)
    main_menu.set_relative_position(largura * 0.075, largura * 0.075)
    submenu.set_relative_position(largura * 0.075, largura * 0.075)


submenu.add_selector("Resolução", conf.getResolucoes(), 0, onchange=submenu_resolucao)
submenu.add_selector("Cor do Tabuleiro", conf.getCoresTabulerio(), 0, onchange=submenu_cores)
main_menu.add_button('Configurações', submenu)
main_menu.add_button('Sobre', sobreOJogo)
main_menu.add_button('Quit', pygame_menu.events.EXIT)
main_menu.add_image("jogo-damas.jpg", angle=10, scale=(0.15, 0.15))
main_menu.mainloop(gamedisplay)
