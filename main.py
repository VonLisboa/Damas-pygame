import pygame
from pygame_menu import Menu

from Bot import *
from Jogo import Jogo
from MenuCustom import MenuCustom
import pygame_menu
from constantes import Cores
from Configurations import Configurations
from constantes import tema


def getMouseCoordenadas(tamQuadrado):
    x, y = pygame.mouse.get_pos()
    lin = y // tamQuadrado
    col = x // tamQuadrado
    return int(lin), int(col)




def main():
    global conf
    global gamedisplay

    running = True
    clock = pygame.time.Clock()
    jogo = Jogo(gamedisplay, conf)

    pygame.display.update()
    while running:
        clock.tick(10)

        if jogo.vez == conf.corPA:
            novo_tabuleiro = bot_joga(jogo.tabuleiro, jogo, conf)
            # jogo.bot_movimentou(novo_tabuleiro)

        if jogo.ganhador() is not None:
            print(jogo.ganhador())
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                lin, col = getMouseCoordenadas(conf.getTamanhoQuadrado())
                jogo.seleciona(lin, col)

        jogo.update()
        pygame.display.update()

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


def submenu_cores_peca(txt, i):
    conf.setCorPeca(i)


def submenu_resolucao(txt, i):
    global main_menu, submenu
    largura, altura = conf.setResolucao(i)
    main_menu.set_relative_position(largura * 0.075, largura * 0.075)
    submenu.set_relative_position(largura * 0.075, largura * 0.075)


submenu.add_selector("Resolução", conf.getResolucoes(), 0, onchange=submenu_resolucao)
submenu.add_selector("Cor do Tabuleiro", conf.getCoresTabulerio(), 0, onchange=submenu_cores)
submenu.add_selector("Cor da Peça", conf.getCoresPeca(), 0, onchange=submenu_cores_peca)
main_menu.add_button('Configurações', submenu)
main_menu.add_button('Sobre', sobreOJogo)
main_menu.add_button('Quit', pygame_menu.events.EXIT)
main_menu.add_image("jogo-damas.jpg", angle=10, scale=(0.15, 0.15))
main_menu.mainloop(gamedisplay)
