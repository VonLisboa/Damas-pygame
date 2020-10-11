import pygame
import pygame_menu



#Dimensões
largura = 400
altura = 400
linhas = 8
colunas = 8
quadrado = 50

#Cores
vermelho = (255, 0, 0)
branco = (255, 255, 255)
preto = (0, 0, 0)
azul = (0, 0, 255)
rosaClaro = (255, 204, 255)
verdeClaro = (204, 255, 204)


#Tema Menu
tema = pygame_menu.themes.THEME_DEFAULT
tema.cursor_color = (255, 100, 255)
tema.title_font_size = 40
tema.title_font = 'comicsansms'
